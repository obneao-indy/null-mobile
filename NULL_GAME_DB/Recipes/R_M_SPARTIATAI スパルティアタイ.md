---
type: null-recipe
id: R_M_SPARTIATAI
name: スパルティアタイ
---

# スパルティアタイ

## Data

このJSONブロックがゲームDBへ出力されます。キー名は変更せず、値を編集してください。

```json
{
  "id": "R_M_SPARTIATAI",
  "name": "スパルティアタイ",
  "kind": "monster",
  "result": {
    "type": "monster",
    "id": "M_SPARTIATAI"
  },
  "requires": [
    {
      "id": "M_GARDNER",
      "level": 3,
      "count": 3
    },
    {
      "id": "M_HELME",
      "level": 3,
      "count": 3
    },
    {
      "id": "M_GARDNER",
      "level": 1,
      "count": 2
    },
    {
      "id": "M_HELME",
      "level": 1,
      "count": 2
    }
  ]
}
```
