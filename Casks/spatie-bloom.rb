cask "spatie-bloom" do
  version "1.40.2"
  sha256 "4d017f363532fb4c3f3d15570dc0b06460fc1b54f5db87370676205cd016ec45"

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
