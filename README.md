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
