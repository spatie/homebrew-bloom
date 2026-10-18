cask "spatie-bloom" do
  version "1.39.1"
  sha256 "eed37490159f4029af8209084f5a2f49078d040c0ac5e841dbbd74b3a05e749c"

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
