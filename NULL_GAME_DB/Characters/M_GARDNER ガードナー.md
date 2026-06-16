---
type: null-character
id: M_GARDNER
name: ガードナー
---

# ガードナー

敵の攻撃を引き付けて味方を守る盾型キャラクター。

## Visual

![[Assets/Characters/gardner.png]]

## Data

このJSONブロックがゲームDBへ出力されます。キー名は変更せず、値を編集してください。

```json
{
  "id": "M_GARDNER",
  "name": "ガードナー",
  "glyph": "◆",
  "hp": 20,
  "speed": 3,
  "slots": 1,
  "trait": null,
  "visual": {
    "src": "assets/characters/gardner.png",
    "vaultSrc": "Assets/Characters/gardner.png",
    "w": 50,
    "h": 58,
    "y": -5
  },
  "levels": {
    "2": {
      "hp": 20,
      "speed": 3
    },
    "3": {
      "hp": 30,
      "speed": 3,
      "trait": "gather"
    }
  },
  "desc": "敵の攻撃を引き付けて味方を守る盾型キャラクター。"
}
```
