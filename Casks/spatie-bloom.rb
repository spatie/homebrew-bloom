cask "spatie-bloom" do
  version "1.41.1"
  sha256 "26be83437837c897b9809b49b3a1c2a2baabd894cd550c0052b598cd9b54310d"

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
