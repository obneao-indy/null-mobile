---
type: null-character
id: M_HELME
name: ヘルメ
---

# ヘルメ

兜をモチーフとしたキャラクター。攻撃を受けると反撃する。

## Visual

![[Assets/Characters/helme.png]]

## Data

このJSONブロックがゲームDBへ出力されます。キー名は変更せず、値を編集してください。

```json
{
  "id": "M_HELME",
  "name": "ヘルメ",
  "glyph": "兜",
  "hp": 20,
  "speed": 10,
  "slots": 2,
  "trait": null,
  "visual": {
    "src": "assets/characters/helme.png",
    "vaultSrc": "Assets/Characters/helme.png",
    "w": 42,
    "h": 66,
    "y": -7
  },
  "levels": {
    "2": {
      "hp": 15,
      "speed": 15
    },
    "3": {
      "hp": 10,
      "speed": 15,
      "trait": "counter"
    }
  },
  "desc": "兜をモチーフとしたキャラクター。攻撃を受けると反撃する。"
}
```
