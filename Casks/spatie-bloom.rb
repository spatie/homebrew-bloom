cask "spatie-bloom" do
  version "1.9.0"
  sha256 "19dbd339719f2ab6ceb04e1b02ecbb3cca5f3229d9755555e64dc7dd4e902e7d"

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
