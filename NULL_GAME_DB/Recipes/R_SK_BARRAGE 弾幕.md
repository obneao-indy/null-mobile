---
type: null-recipe
id: R_SK_BARRAGE
name: 弾幕
---

# 弾幕

## Data

このJSONブロックがゲームDBへ出力されます。キー名は変更せず、値を編集してください。

```json
{
  "id": "R_SK_BARRAGE",
  "name": "弾幕",
  "kind": "skill",
  "result": {
    "type": "skill",
    "id": "SK_BARRAGE"
  },
  "requires": [
    {
      "id": "M_BLACKCIRCLE",
      "count": 5
    }
  ]
}
```
