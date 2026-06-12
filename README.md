# NULL mobile playtest

Static mobile playtest build for `NULL`.

## Play

https://obneao-indy.github.io/null-mobile/

## Run locally

```powershell
node server.mjs
```

## External game database

`NULL_game_db.xlsx` is the editable master database. Export it after editing:

```powershell
python tools/export_game_db.py --workbook NULL_game_db.xlsx --output game_db.json --export-only
```

The game loads `game_db.json` on startup and falls back to the inline definitions if the file cannot be loaded.

New content can be drafted in the yellow cells of these sheets:

- `TEMPLATE_CHARACTER`
- `TEMPLATE_SKILL`
- `TEMPLATE_STAGE`
- `TEMPLATE_DROP`
- `TEMPLATE_RECIPE`

After the design is confirmed, transfer the entries to the corresponding normalized DB sheets and export the JSON.

For chat-based requests, copy and fill in [NEW_CONTENT_CHAT_TEMPLATE.md](NEW_CONTENT_CHAT_TEMPLATE.md). It includes character levels, traits, multiple related skills, skill-level changes, exact character-level drops, recipes, and stages.
