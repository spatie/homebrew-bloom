# Homebrew tap for Bloom

Install [Bloom](https://runbloom.app), Spatie's native Mac environment for coding agents:

```sh
brew install --cask spatie/bloom/spatie-bloom
```

Requires Apple Silicon and macOS 26 or later. The cask is named `spatie-bloom` because
Homebrew already has an unrelated file manager named `bloom`. Both apps use
`Bloom.app`, so the casks cannot be installed together.

Bloom checks for updates itself. To upgrade through Homebrew:

```sh
brew update
brew upgrade --cask --greedy spatie/bloom/spatie-bloom
```

The update workflow checks [Bloom's appcast](https://downloads.runbloom.app/appcast.xml)
for the latest stable release every hour. It downloads the disk image, checks its
length against the appcast, computes its SHA-256, and commits the new version and
checksum. It can also be run manually from GitHub Actions.

To update locally:

```sh
python3 scripts/update-cask.py
```
