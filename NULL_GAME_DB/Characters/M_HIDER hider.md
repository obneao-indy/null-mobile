---
type: null-character
id: M_HIDER
name: hider
---

# hider

Level3で毎ターン30%の確率で潜伏する。

## Data

このJSONブロックがゲームDBへ出力されます。キー名は変更せず、値を編集してください。

```json
{
  "id": "M_HIDER",
  "name": "hider",
  "glyph": "◎",
  "hp": 10,
  "speed": 15,
  "slots": 2,
  "trait": null,
  "levels": {
    "2": {
      "hp": 10,
      "speed": 10
    },
    "3": {
      "hp": 10,
      "speed": 15,
      "trait": "hide"
    }
  },
  "desc": "Level3で毎ターン30%の確率で潜伏する。"
}
```
