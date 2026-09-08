import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


spec = importlib.util.spec_from_file_location("update_cask", Path(__file__).with_name("update-cask.py"))
updater = importlib.util.module_from_spec(spec)
spec.loader.exec_module(updater)


class UpdateCaskTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        (self.root / "scripts").mkdir()
        (self.root / "Casks").mkdir()
        self.cask = self.root / "Casks/spatie-bloom.rb"
        self.original = 'cask "spatie-bloom" do\n  version "1.4.0"\n  sha256 "old"\nend\n'
        self.cask.write_text(self.original)
        self.release = {
            "tag_name": "v1.5.0", "draft": False, "prerelease": False,
            "assets": [{"name": "Bloom-1.5.0.dmg", "state": "uploaded",
                        "digest": "sha256:" + hashlib.sha256(b"disk image").hexdigest()}],
        }
        self.addCleanup(patch.stopall)
        patch.object(updater, "__file__", str(self.root / "scripts/update-cask.py")).start()
        self.api = patch.object(updater.subprocess, "check_output").start()
        self.download = patch.object(updater.subprocess, "run", side_effect=self.write_download).start()

    def write_download(self, command, **kwargs):
        (Path(command[-1]) / "Bloom-1.5.0.dmg").write_bytes(b"disk image")

    def run_update(self):
        self.api.return_value = json.dumps(self.release)
        updater.main()

    def test_update_verifies_download_and_is_idempotent(self):
        self.run_update()
        self.assertIn('version "1.5.0"', self.cask.read_text())
        self.assertIn(hashlib.sha256(b"disk image").hexdigest(), self.cask.read_text())
        self.run_update()
        self.download.assert_called_once()

    def test_waits_for_release_asset(self):
        self.release["assets"] = []
        self.run_update()
        self.assertEqual(self.original, self.cask.read_text())
        self.download.assert_not_called()

    def test_rejects_prerelease(self):
        self.release["prerelease"] = True
        with self.assertRaises(SystemExit):
            self.run_update()
        self.assertEqual(self.original, self.cask.read_text())

    def test_rejects_invalid_digest(self):
        self.release["assets"][0]["digest"] = None
        with self.assertRaises(SystemExit):
            self.run_update()
        self.assertEqual(self.original, self.cask.read_text())

    def test_rejects_checksum_mismatch(self):
        self.release["assets"][0]["digest"] = "sha256:" + "0" * 64
        with self.assertRaises(SystemExit):
            self.run_update()
        self.assertEqual(self.original, self.cask.read_text())

    def test_refuses_downgrade(self):
        self.cask.write_text(self.original.replace("1.4.0", "1.6.0"))
        with self.assertRaises(SystemExit):
            self.run_update()
        self.download.assert_not_called()


if __name__ == "__main__":
    unittest.main()
