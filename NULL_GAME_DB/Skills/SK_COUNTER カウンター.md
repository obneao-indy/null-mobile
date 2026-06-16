---
type: null-skill
id: SK_COUNTER
name: カウンター
---

# カウンター

効果中、このキャラクターは反撃状態になる。

## Data

このJSONブロックがゲームDBへ出力されます。キー名は変更せず、値を編集してください。

```json
{
  "id": "SK_COUNTER",
  "name": "カウンター",
  "glyph": "↩",
  "desc": "効果中、このキャラクターは反撃状態になる。",
  "counter": true,
  "counterTurns": [
    0,
    2,
    2,
    3
  ],
  "ct": [
    0,
    8,
    6,
    4
  ],
  "target": "self"
}
```
