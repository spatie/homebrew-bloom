import hashlib
import importlib.util
from io import BytesIO
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


spec = importlib.util.spec_from_file_location("update_cask", Path(__file__).with_name("update-cask.py"))
updater = importlib.util.module_from_spec(spec)
spec.loader.exec_module(updater)


def item(version, *, channel="", image=True, url=None, length=None):
    channel_xml = f"<sparkle:channel>{channel}</sparkle:channel>" if channel else ""
    image_xml = ""
    if image:
        image_url = url or f"{updater.DOWNLOAD_BASE}/Bloom-{version}.dmg"
        image_length = length if length is not None else len(b"disk image")
        image_xml = f'<bloom:diskImage url="{image_url}" length="{image_length}" />'
    return f"<item><sparkle:shortVersionString>{version}</sparkle:shortVersionString>{channel_xml}{image_xml}</item>"


def feed(*items):
    return (f'<rss xmlns:sparkle="{updater.SPARKLE}" xmlns:bloom="{updater.BLOOM}">'
            f'<channel>{"".join(items)}</channel></rss>').encode()


class UpdateCaskTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        root = Path(self.directory.name)
        (root / "scripts").mkdir()
        (root / "Casks").mkdir()
        self.cask = root / "Casks/spatie-bloom.rb"
        self.original = 'cask "spatie-bloom" do\n  version "1.4.0"\n  sha256 "old"\nend\n'
        self.cask.write_text(self.original)
        self.feed = feed(item("1.5.0"))
        self.image = b"disk image"
        self.addCleanup(patch.stopall)
        patch.object(updater, "__file__", str(root / "scripts/update-cask.py")).start()
        self.open_url = patch.object(updater, "urlopen", side_effect=self.open_response).start()

    def open_response(self, url, **kwargs):
        if url == updater.FEED_URL:
            return BytesIO(self.feed)
        if url == f"{updater.DOWNLOAD_BASE}/Bloom-1.5.0.dmg":
            return BytesIO(self.image)
        self.fail(f"Unexpected download: {url}")

    def test_updates_from_stable_image_and_is_idempotent(self):
        self.feed = feed(item("1.6.0", channel="beta"), item("1.5.0"))
        updater.main()
        self.assertIn('version "1.5.0"', self.cask.read_text())
        self.assertIn(hashlib.sha256(self.image).hexdigest(), self.cask.read_text())
        updater.main()
        self.assertEqual(self.open_url.call_count, 4)

    def test_waits_for_latest_stable_image(self):
        self.feed = feed(item("1.5.0", image=False), item("1.4.0"))
        updater.main()
        self.assertEqual(self.original, self.cask.read_text())
        self.open_url.assert_called_once()

    def test_rejects_unexpected_image_url(self):
        self.feed = feed(item("1.5.0", url="https://example.com/Bloom-1.5.0.dmg"))
        with self.assertRaises(SystemExit):
            updater.main()
        self.assertEqual(self.original, self.cask.read_text())

    def test_rejects_incomplete_download(self):
        self.feed = feed(item("1.5.0", length=20))
        with self.assertRaises(SystemExit):
            updater.main()
        self.assertEqual(self.original, self.cask.read_text())

    def test_refuses_downgrade(self):
        self.cask.write_text(self.original.replace("1.4.0", "1.6.0"))
        with self.assertRaises(SystemExit):
            updater.main()
        self.open_url.assert_called_once()


if __name__ == "__main__":
    unittest.main()
