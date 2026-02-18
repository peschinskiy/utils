# Claude Code Guidelines

## After any changes

- **Keep README, repo, and `utils` in sync**: The Scripts table in `README.md`, the actual files in `bin/` and `fish/`, and the entries printed by the `utils` script must always match. Add, remove, or update all three together.
- **Run tests**: After modifying any script, run `cd tests && pytest` to verify nothing is broken.
- **Update tests**: If you add or meaningfully change a script, add or update the corresponding tests in `tests/`.
