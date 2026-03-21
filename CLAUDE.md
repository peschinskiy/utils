# Claude Code Guidelines

## Repo structure

This is a dotfiles repo managed with [GNU stow](https://www.gnu.org/software/stow/). Each top-level directory is a stow package that mirrors the home directory layout:

- `bin/` — scripts; `bin/bin/` maps to `~/bin/`
- `fish/` — Fish shell config; `fish/.config/fish/` maps to `~/.config/fish/`

## After any changes

- **Keep README and `utils` in sync**: The Scripts table in `README.md` and the entries printed by the `utils` script must always match. Add, remove, or update both together.
