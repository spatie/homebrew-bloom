cask "spatie-bloom" do
  version "1.39.3"
  sha256 "94d05b0df93f2acb734b949a14455e357a3fbe192c647124aa097d7e464114ef"

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
