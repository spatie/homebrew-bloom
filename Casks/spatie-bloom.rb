cask "spatie-bloom" do
  version "1.40.0"
  sha256 "c50fad25cd5cde7a1be5543c2e6ec9bde3693252f6c3c303f10911f059d94b2e"

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
