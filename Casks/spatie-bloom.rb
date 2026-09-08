cask "spatie-bloom" do
  version "1.5.1"
  sha256 "eb5b212d0c88dbf5753137048d487df386c7e6bcee7567d1b13f022696630f2e"

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
