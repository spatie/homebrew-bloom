cask "spatie-bloom" do
  version "1.16.1"
  sha256 "50d849e9860f9e455a471e40b73000706b4461c0ed7aa6e1236040af84a3d280"

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
