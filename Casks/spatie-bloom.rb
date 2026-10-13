cask "spatie-bloom" do
  version "1.38.18"
  sha256 "1a9466e6af069937ec71a6b4128d4e9016bca27c9a5121447a1da413d94c1448"

  url "https://downloads.runbloom.app/Bloom-#{version}.dmg"
  name "Bloom"
  desc "Agent development environment"
  homepage "https://runbloom.app/"

  auto_updates true
  conflicts_with cask: "bloom"
  depends_on arch: :arm64
  depends_on macos: :tahoe

  app "Bloom.app"
end
