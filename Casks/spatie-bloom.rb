cask "spatie-bloom" do
  version "1.39.2"
  sha256 "beeb643791899175639004c9253898cacb6ff8e32c716319e8107904ee7f297b"

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
