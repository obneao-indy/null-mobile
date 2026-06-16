---
type: null-character
id: M_OUMUAMUA
name: オウムアムア
---

# オウムアムア

高速で突入する異形。Level3で光速突進を行う。

## Visual

![[Assets/Characters/oumuamua.png]]

## Data

このJSONブロックがゲームDBへ出力されます。キー名は変更せず、値を編集してください。

```json
{
  "id": "M_OUMUAMUA",
  "name": "オウムアムア",
  "glyph": "◉",
  "hp": 30,
  "speed": 50,
  "slots": 3,
  "trait": null,
  "visual": {
    "src": "assets/characters/oumuamua.png",
    "w": 22,
    "h": 86,
    "y": -15,
    "orientation": "sphere-trail-up",
    "vaultSrc": "Assets/Characters/oumuamua.png"
  },
  "levels": {
    "2": {
      "hp": 20,
      "speed": 30,
      "trait": "barrage"
    },
    "3": {
      "hp": 20,
      "speed": 40,
      "trait": "lightRush"
    }
  },
  "desc": "高速で突入する異形。Level3で光速突進を行う。"
}
```
