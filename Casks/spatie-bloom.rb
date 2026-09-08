cask "spatie-bloom" do
  version "1.5.0"
  sha256 "2cfa295647971209631b021abda575d71936243ba3a1ee09cd2a53458001ba54"

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
  depends_on macos: ">= :tahoe"

  app "Bloom.app"
end
