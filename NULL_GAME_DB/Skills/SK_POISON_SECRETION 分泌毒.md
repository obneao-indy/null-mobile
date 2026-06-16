---
type: null-skill
id: SK_POISON_SECRETION
name: 分泌毒
---

# 分泌毒

通常攻撃後、対象へ毒を確定付与。

## Data

このJSONブロックがゲームDBへ出力されます。キー名は変更せず、値を編集してください。

```json
{
  "id": "SK_POISON_SECRETION",
  "name": "分泌毒",
  "glyph": "♟",
  "desc": "通常攻撃後、対象へ毒を確定付与。",
  "target": "enemy",
  "targets": 1,
  "poisonAttack": true,
  "poisonTurns": [
    0,
    2,
    2,
    3
  ],
  "ct": [
    0,
    6,
    5,
    4
  ]
}
```
