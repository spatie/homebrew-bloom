cask "spatie-bloom" do
  version "1.40.4"
  sha256 "2fa08e77ee3210b6780d6548b77782a5f566cb1ca0f76c297164ee701429f1b4"

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
