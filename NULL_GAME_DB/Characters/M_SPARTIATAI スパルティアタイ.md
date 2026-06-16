---
type: null-character
id: M_SPARTIATAI
name: スパルティアタイ
---

# スパルティアタイ

盾と兜が特徴のスパルタの戦士。防御と反撃、怒りの一撃を備える。

## Visual

![[Assets/Characters/spartiatai.png]]

## Data

このJSONブロックがゲームDBへ出力されます。キー名は変更せず、値を編集してください。

```json
{
  "id": "M_SPARTIATAI",
  "name": "スパルティアタイ",
  "glyph": "Σ",
  "hp": 40,
  "speed": 20,
  "slots": 0,
  "trait": "gather",
  "visual": {
    "src": "assets/characters/spartiatai.png",
    "vaultSrc": "Assets/Characters/spartiatai.png",
    "w": 66,
    "h": 74,
    "y": -6
  },
  "levels": {
    "2": {
      "hp": 30,
      "speed": 20,
      "trait": "counter"
    },
    "3": {
      "hp": 30,
      "speed": 20,
      "trait": "spartanRage"
    }
  },
  "desc": "盾と兜が特徴のスパルタの戦士。防御と反撃、怒りの一撃を備える。"
}
```
