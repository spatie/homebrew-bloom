#!/usr/bin/env python3
"""Update the cask only after a stable release's disk image is available."""

import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile


def main():
    release = json.loads(subprocess.check_output(
        ["gh", "api", "repos/spatie/bloom/releases/latest"], text=True,
    ))
    tag = release["tag_name"]
    if release["draft"] or release["prerelease"] or not re.fullmatch(r"v\d+\.\d+\.\d+", tag):
        raise SystemExit("The latest release is not a stable version.")

    version = tag[1:]
    name = f"Bloom-{version}.dmg"
    asset = next((asset for asset in release["assets"] if asset["name"] == name), None)
    if asset is None or asset["state"] != "uploaded":
        print(f"Waiting for {name} to be uploaded.")
        return

    digest = asset.get("digest") or ""
    if not re.fullmatch(r"sha256:[0-9a-f]{64}", digest):
        raise SystemExit("The disk image has no valid SHA-256 digest.")
    checksum = digest.removeprefix("sha256:")
    cask = Path(__file__).resolve().parents[1] / "Casks/spatie-bloom.rb"
    original = cask.read_text()
    current = re.search(r'^  version "(\d+\.\d+\.\d+)"$', original, re.MULTILINE)
    if current is None:
        raise SystemExit("Cannot find the current cask version.")
    if tuple(map(int, version.split("."))) < tuple(map(int, current[1].split("."))):
        raise SystemExit("Refusing to downgrade the cask.")
    updated, versions = re.subn(r'^  version ".*"$', f'  version "{version}"', original, flags=re.MULTILINE)
    updated, checksums = re.subn(r'^  sha256 ".*"$', f'  sha256 "{checksum}"', updated, flags=re.MULTILINE)
    if versions != 1 or checksums != 1:
        raise SystemExit("Expected exactly one version and checksum.")
    if updated == original:
        print(f"Bloom {version} is already current.")
        return

    with tempfile.TemporaryDirectory() as directory:
        subprocess.run([
            "gh", "release", "download", tag, "--repo", "spatie/bloom",
            "--pattern", name, "--dir", directory,
        ], check=True)
        actual = hashlib.sha256((Path(directory) / name).read_bytes()).hexdigest()
        if actual != checksum:
            raise SystemExit("The downloaded disk image does not match GitHub's checksum.")

    cask.write_text(updated)
    print(f"Updated Bloom to {version}.")


if __name__ == "__main__":
    main()
