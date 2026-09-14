cask "spatie-bloom" do
  version "1.17.1"
  sha256 "06adcfe93aded6e02c6510b3659a80deb6c94ee7666fde7bda7d9ec8f3b0eb83"

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
