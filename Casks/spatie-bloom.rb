cask "spatie-bloom" do
  version "1.40.1"
  sha256 "8c61a0a141b75f52225fdef2aa4aa621e4b6d520d72afc2620ff1b45e523b51f"

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
