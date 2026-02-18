#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
BIN_TARGET="${HOME}/.local/bin"
FISH_TARGET="${HOME}/.config/fish"

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
while IFS= read -r -d '' func; do
    relative_path="${func#$REPO_DIR/fish/}"
    target_file="$FISH_TARGET/$relative_path"
    mkdir -p "$(dirname "$target_file")"
    link "$func" "$target_file"
done < <(find "$REPO_DIR/fish/" -type f -name "*.fish" -print0)

echo "Done."
