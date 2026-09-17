cask "spatie-bloom" do
  version "1.30.0"
  sha256 "c4529ae76ec199cece698fab945b1ba083d92e31028fc7c26c05fc9b1b80b0c5"

  url "https://github.com/spatie/bloom/releases/download/v#{version}/Bloom-#{version}.dmg",
      verified: "github.com/spatie/bloom/"
  name "Bloom"
  desc "Agent development environment"
  homepage "https://runbloom.app/"

  livecheck do
    url :url
    strategy :github_latest
  end

  auto_updates true
  conflicts_with cask: "bloom"
  depends_on arch: :arm64
  depends_on macos: :tahoe

  app "Bloom.app"
end
