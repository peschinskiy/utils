#!/usr/bin/env bash
set -euo pipefail
shopt -s globstar

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
BIN_TARGET="${HOME}/.local/bin"
FISH_TARGET="${HOME}/.config/fish"
FISH_FUNCTIONS_TARGET="${HOME}/.config/fish/functions"

link() {
	local src="$1"
	local dst="$2"
	ln -sf "$src" "$dst"
	echo "  linked $(basename "$dst")"
}

echo "Installing scripts -> $BIN_TARGET"
mkdir -p "$BIN_TARGET"
for script in "$REPO_DIR/bin/"*; do
	chmod +x "$script"
	link "$script" "$BIN_TARGET/$(basename "$script")"
done

echo "Installing fish functions -> $FISH_TARGET"
mkdir -p "$FISH_FUNCTIONS_TARGET"
for func in "$REPO_DIR/fish/"**/*.fish; do
	link "$func" "$FISH_TARGET/$(basename "$func")"
done

echo "Done."
