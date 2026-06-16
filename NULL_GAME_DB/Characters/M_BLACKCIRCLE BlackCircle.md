---
type: null-character
id: M_BLACKCIRCLE
name: BlackCircle
---

# BlackCircle

Level3で通常攻撃が2体対象になる高速個体。

## Data

このJSONブロックがゲームDBへ出力されます。キー名は変更せず、値を編集してください。

```json
{
  "id": "M_BLACKCIRCLE",
  "name": "BlackCircle",
  "glyph": "●",
  "hp": 10,
  "speed": 10,
  "slots": 3,
  "trait": null,
  "levels": {
    "2": {
      "hp": 10,
      "speed": 5
    },
    "3": {
      "hp": 10,
      "speed": 5,
      "trait": "scatter"
    }
  },
  "desc": "Level3で通常攻撃が2体対象になる高速個体。"
}
```
