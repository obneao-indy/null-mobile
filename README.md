# NULL mobile playtest

Static mobile playtest build for `NULL`.

## Play

https://obneao-indy.github.io/null-mobile/

## Run locally

```powershell
node server.mjs
```

## External game database

`NULL_GAME_DB` is the editable master database. Open that folder as an Obsidian Vault, edit the Markdown notes, then export:

```powershell
python tools/markdown_game_db.py export --vault NULL_GAME_DB --output game_db.json
```

Each character, trait, skill, stage, and recipe has its own note. Human-readable descriptions and the machine-readable JSON block live in the same Markdown file.

`NULL_game_db.xlsx` remains as a compatibility backup. To regenerate JSON from Excel:

```powershell
python tools/export_game_db.py --workbook NULL_game_db.xlsx --output game_db.json --export-only
```

The game loads `game_db.json` on startup and falls back to the inline definitions if the file cannot be loaded.

Excel draft sheets:

- `TEMPLATE_CHARACTER`
- `TEMPLATE_SKILL`
- `TEMPLATE_STAGE`
- `TEMPLATE_DROP`
- `TEMPLATE_RECIPE`

After the design is confirmed, transfer the entries to the corresponding normalized DB sheets and export the JSON.

For chat-based requests, copy and fill in [NEW_CONTENT_CHAT_TEMPLATE.md](NEW_CONTENT_CHAT_TEMPLATE.md). It includes character levels, traits, multiple related skills, skill-level changes, exact character-level drops, recipes, and stages.
