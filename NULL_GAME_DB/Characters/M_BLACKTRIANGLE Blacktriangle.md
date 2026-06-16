---
type: null-character
id: M_BLACKTRIANGLE
name: Blacktriangle
---

# Blacktriangle

Level3で通常攻撃が同じ敵への3連射になる。

## Data

このJSONブロックがゲームDBへ出力されます。キー名は変更せず、値を編集してください。

```json
{
  "id": "M_BLACKTRIANGLE",
  "name": "Blacktriangle",
  "glyph": "▲",
  "hp": 15,
  "speed": 10,
  "slots": 2,
  "trait": null,
  "levels": {
    "2": {
      "hp": 10,
      "speed": 10
    },
    "3": {
      "hp": 20,
      "speed": 5,
      "trait": "rapid"
    }
  },
  "desc": "Level3で通常攻撃が同じ敵への3連射になる。"
}
```
