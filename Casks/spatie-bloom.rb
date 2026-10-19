cask "spatie-bloom" do
  version "1.39.4"
  sha256 "ba3644b2916097cf03283f9e0ca25a0f65324c3f8191d3ccaf1e4f2220e4378b"

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
