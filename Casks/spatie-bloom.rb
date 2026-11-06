cask "spatie-bloom" do
  version "1.39.7"
  sha256 "6ba9be8fbe6e78feed22f4aceda3f4388837db9c55bbc262890c70b88d8316cd"

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
