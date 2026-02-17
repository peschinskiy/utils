# utils

Personal shell utilities. Scripts live in `bin/`, Fish shell functions in `fish/`.

Inspired by [Evan Hahn's approach](https://evanhahn.com/scripts-i-wrote-that-i-use-all-the-time/): prefer scripts in `~/.local/bin` over aliases — no shell reload needed, any language, works across all shells.

## Install

```sh
./install.sh
```

Symlinks everything into `~/.local/bin` (scripts) and `~/.config/fish/functions` (fish functions).

## Scripts

| Script | Description |
|---|---|
| `alphabet` | Print the alphabet in lower and uppercase |
| `copy` | Pipe stdin to clipboard |
| `cpwd` | Copy current directory path to clipboard |
| `getsubs` | Extract English subtitles from a video URL (requires `yt-dlp`) |
| `httpstatus` | List HTTP status codes; optionally filter by code or phrase |
| `ipy` | Python 3 REPL |
| `isql` | SQLite in-memory REPL |
| `line` | Output line N from stdin |
| `lowered` | Convert stdin to lowercase |
| `mksh` | Scaffold a new executable bash script and open in `$EDITOR` |
| `notify` | Send a desktop notification |
| `pasta` | Print clipboard contents to stdout |
| `pastas` | Watch clipboard and print on change |
| `scratch` | Open a throwaway temp file in `$EDITOR` |
| `snippets` | Retrieve stored text snippets from `~/.config/snippets/` |
| `timer` | Countdown timer with notification (`timer 10m`) |
| `trash` | Move files to trash instead of deleting |
| `uppered` | Convert stdin to uppercase |
| `url` | Parse a URL into its components |
| `uuid` | Generate a v4 UUID |
| `ymd` | Print today's date as `YYYY-MM-DD` |

## Fish functions

| Function | Description |
|---|---|
| `boop` | Notify success/failure of the previous command |
| `mkcd` | Create a directory and cd into it |
| `tempe` | cd into a new temporary directory |

## Tests

```sh
cd tests && pytest
```

Requires `pytest` (`pip install pytest` or via `uv`).

## Notes

- Clipboard (`copy`/`pasta`/`pastas`/`cpwd`) uses `clip.exe`/PowerShell on WSL2, with fallbacks for `xclip` and `wl-clipboard` on native Linux.
- `snippets` reads from `~/.config/snippets/`. Create that directory and add plain text files as snippets.
- `timer` uses GNU `sleep` duration syntax: `30s`, `10m`, `1h`, `1h30m`.
