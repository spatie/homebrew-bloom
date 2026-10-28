cask "spatie-bloom" do
  version "1.39.6"
  sha256 "3d7916df54469f02ebb0e2ec51aeba37d4a724a2cbb74e78a3b476c87ea5a376"

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
