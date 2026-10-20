cask "spatie-bloom" do
  version "1.39.5"
  sha256 "bb57e3cdf3bc0da6942bbf0adef4bd11b37e63b476bef12034638016a03a9be4"

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
