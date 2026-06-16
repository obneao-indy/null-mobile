---
type: null-character
id: M_POZ
name: ポズ
---

# ポズ

通常攻撃で毒を分泌する状態異常型個体。

## Data

このJSONブロックがゲームDBへ出力されます。キー名は変更せず、値を編集してください。

```json
{
  "id": "M_POZ",
  "name": "ポズ",
  "glyph": "♟",
  "hp": 10,
  "speed": 10,
  "slots": 1,
  "trait": "poisonSecretion",
  "visual": {
    "src": "assets/characters/poz.png",
    "w": 66,
    "h": 58,
    "y": -5
  },
  "levels": {
    "2": {
      "hp": 6,
      "speed": 15
    },
    "3": {
      "hp": 7,
      "speed": 15
    }
  },
  "desc": "通常攻撃で毒を分泌する状態異常型個体。"
}
```
