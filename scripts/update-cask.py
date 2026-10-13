#!/usr/bin/env python3
"""Update the cask from the latest stable disk image in Bloom's appcast."""

import hashlib
from pathlib import Path
import re
from urllib.request import urlopen
import xml.etree.ElementTree as ET


FEED_URL = "https://downloads.runbloom.app/appcast.xml"
DOWNLOAD_BASE = "https://downloads.runbloom.app"
SPARKLE = "http://www.andymatuschak.org/xml-namespaces/sparkle"
BLOOM = "https://runbloom.app/xml-namespaces/bloom"


def latest_stable_image(feed):
    root = ET.fromstring(feed)
    for item in root.findall("./channel/item"):
        if item.findtext(f"{{{SPARKLE}}}channel"):
            continue

        version = item.findtext(f"{{{SPARKLE}}}shortVersionString") or ""
        if not re.fullmatch(r"\d+\.\d+\.\d+", version):
            raise SystemExit(f"Unexpected stable version in appcast: {version!r}")

        image = item.find(f"{{{BLOOM}}}diskImage")
        if image is None:
            print(f"Waiting for Bloom {version}'s disk image.")
            return None

        url = f"{DOWNLOAD_BASE}/Bloom-{version}.dmg"
        if image.get("url") != url:
            raise SystemExit(f"Unexpected disk image URL for Bloom {version}.")
        length = image.get("length") or ""
        if not length.isdecimal() or int(length) <= 0:
            raise SystemExit(f"Invalid disk image length for Bloom {version}.")
        return version, url, int(length)

    raise SystemExit("No stable release in Bloom's appcast.")


def disk_image_checksum(url, expected_length):
    digest = hashlib.sha256()
    size = 0
    with urlopen(url, timeout=60) as image:
        while chunk := image.read(1024 * 1024):
            size += len(chunk)
            if size > expected_length:
                raise SystemExit("Disk image exceeds its appcast length.")
            digest.update(chunk)
    if size != expected_length:
        raise SystemExit("Disk image does not match its appcast length.")
    return digest.hexdigest()


def main():
    with urlopen(FEED_URL, timeout=20) as response:
        release = latest_stable_image(response.read())
    if release is None:
        return
    version, url, length = release

    cask = Path(__file__).resolve().parents[1] / "Casks/spatie-bloom.rb"
    original = cask.read_text()
    current = re.search(r'^  version "(\d+\.\d+\.\d+)"$', original, re.MULTILINE)
    if current is None:
        raise SystemExit("Cannot find the current cask version.")
    if tuple(map(int, version.split("."))) < tuple(map(int, current[1].split("."))):
        raise SystemExit("Refusing to downgrade the cask.")

    checksum = disk_image_checksum(url, length)
    updated, versions = re.subn(r'^  version ".*"$', f'  version "{version}"', original, flags=re.MULTILINE)
    updated, checksums = re.subn(r'^  sha256 ".*"$', f'  sha256 "{checksum}"', updated, flags=re.MULTILINE)
    if versions != 1 or checksums != 1:
        raise SystemExit("Expected exactly one version and checksum.")
    if updated == original:
        print(f"Bloom {version} is already current.")
        return

    cask.write_text(updated)
    print(f"Updated Bloom to {version}.")


if __name__ == "__main__":
    main()
