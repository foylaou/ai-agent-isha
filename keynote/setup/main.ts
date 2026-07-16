// No longer used — icons are now provided via Slidev's built-in Iconify
// support (see @iconify-json/lucide in package.json) instead of manually
// registering @lucide/vue components here. Registering plain component
// names like `WifiOff` collided with unplugin-icons' auto icon resolution
// (it parsed "WifiOff" as collection "wi" + icon "fi-off" and crashed),
// so this approach was replaced with <lucide-xxx /> tags directly in
// slides.md, which is the officially supported pattern.
export default function setup() {}
