cask "spatie-bloom" do
  version "1.18.0"
  sha256 "00568bfd93d8879b4c11e925fe512d5d6286e533c7b3efcc45f6882fb7cd0ab6"

  url "https://github.com/spatie/bloom/releases/download/v#{version}/Bloom-#{version}.dmg"
  name "Bloom"
  desc "Agent development environment"
  homepage "https://runbloom.app/"

  livecheck do
    url :url
    strategy :github_latest
  end

  auto_updates true
  conflicts_with cask: "bloom"
  depends_on arch: :arm64
  depends_on macos: :tahoe

  app "Bloom.app"
end
