---
type: null-character
id: M_HAMMER
name: ハンマー
---

# ハンマー

1ターン溜めて強打を行う低速個体。

## Visual

![[Assets/Characters/hammer.png]]

## Data

このJSONブロックがゲームDBへ出力されます。キー名は変更せず、値を編集してください。

```json
{
  "id": "M_HAMMER",
  "name": "ハンマー",
  "glyph": "T",
  "hp": 10,
  "speed": 5,
  "slots": 1,
  "trait": null,
  "visual": {
    "src": "assets/characters/hammer.png",
    "w": 46,
    "h": 68,
    "y": -6,
    "vaultSrc": "Assets/Characters/hammer.png"
  },
  "levels": {
    "2": {
      "hp": 10,
      "speed": 5
    },
    "3": {
      "hp": 15,
      "speed": 5,
      "trait": "heavyStrike"
    }
  },
  "desc": "1ターン溜めて強打を行う低速個体。"
}
```
