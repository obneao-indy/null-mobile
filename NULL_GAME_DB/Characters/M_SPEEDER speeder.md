---
type: null-character
id: M_SPEEDER
name: speeder
---

# speeder

Level3でスピードが20%上昇する。

## Data

このJSONブロックがゲームDBへ出力されます。キー名は変更せず、値を編集してください。

```json
{
  "id": "M_SPEEDER",
  "name": "speeder",
  "glyph": "▲",
  "hp": 10,
  "speed": 20,
  "slots": 2,
  "trait": null,
  "levels": {
    "2": {
      "hp": 10,
      "speed": 15
    },
    "3": {
      "hp": 10,
      "speed": 15,
      "trait": "dash"
    }
  },
  "desc": "Level3でスピードが20%上昇する。"
}
```
