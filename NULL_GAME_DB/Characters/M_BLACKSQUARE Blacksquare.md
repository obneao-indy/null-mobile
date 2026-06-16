---
type: null-character
id: M_BLACKSQUARE
name: Blacksquare
---

# Blacksquare

Level3でワイドガードを獲得する基礎個体。

## Data

このJSONブロックがゲームDBへ出力されます。キー名は変更せず、値を編集してください。

```json
{
  "id": "M_BLACKSQUARE",
  "name": "Blacksquare",
  "glyph": "■",
  "hp": 20,
  "speed": 10,
  "slots": 2,
  "trait": null,
  "levels": {
    "2": {
      "hp": 10,
      "speed": 5
    },
    "3": {
      "hp": 20,
      "speed": 5,
      "trait": "wideGuard"
    }
  },
  "desc": "Level3でワイドガードを獲得する基礎個体。"
}
```
