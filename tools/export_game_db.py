import argparse
import json
import shutil
from datetime import datetime
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.table import Table, TableStyleInfo


SHEETS = {
    "characters": [
        "monster_id", "name", "glyph", "base_hp", "base_speed", "slots",
        "base_trait", "description",
    ],
    "character_levels": [
        "monster_id", "level", "hp_add", "speed_add", "trait_id",
    ],
    "traits": ["trait_id", "name", "description"],
    "skills": [
        "skill_id", "name", "glyph", "description", "target", "targets",
        "effect_type",
    ],
    "skill_levels": [
        "skill_id", "level", "power", "ct", "hits", "multiplier",
        "guard_pct", "speed_pct", "duration",
    ],
    "stages": [
        "stage_id", "name", "category", "info", "unlock_type",
        "unlock_value",
    ],
    "stage_waves": [
        "stage_id", "wave", "position", "monster_id", "level",
    ],
    "drops": [
        "source_monster_id", "min_level", "drop_type", "drop_id", "rate",
    ],
    "recipes": ["recipe_id", "name", "result_type", "result_id"],
    "recipe_materials": [
        "recipe_id", "material_monster_id", "count",
    ],
    "system_rules": ["rule_id", "value", "description"],
}


DATA = {
    "characters": [
        ["M_BLACKSQUARE", "Blacksquare", "■", 20, 10, 2, "", "Level3でワイドガードを獲得する基礎個体。"],
        ["M_BLACKCIRCLE", "BlackCircle", "●", 10, 10, 3, "", "Level3で通常攻撃が2体対象になる高速個体。"],
        ["M_HIDER", "hider", "◎", 10, 15, 2, "", "Level3で毎ターン30%の確率で潜伏する。"],
        ["M_BLACKTRIANGLE", "Blacktriangle", "▲", 15, 10, 2, "", "Level3で通常攻撃が同じ敵への3連射になる。"],
        ["M_SPEEDER", "speeder", "▲", 10, 20, 2, "", "Level3でスピードが20%上昇する。"],
        ["M_OUMUAMUA", "オウムアムア", "◉", 30, 50, 3, "", "高速で突入する異形。Level3で光速突進を行う。"],
    ],
    "character_levels": [
        ["M_BLACKSQUARE", 2, 10, 5, ""], ["M_BLACKSQUARE", 3, 20, 5, "wideGuard"],
        ["M_BLACKCIRCLE", 2, 10, 5, ""], ["M_BLACKCIRCLE", 3, 10, 5, "scatter"],
        ["M_HIDER", 2, 10, 10, ""], ["M_HIDER", 3, 10, 15, "hide"],
        ["M_BLACKTRIANGLE", 2, 10, 10, ""], ["M_BLACKTRIANGLE", 3, 20, 5, "rapid"],
        ["M_SPEEDER", 2, 10, 15, ""], ["M_SPEEDER", 3, 10, 15, "dash"],
        ["M_OUMUAMUA", 2, 20, 30, "barrage"], ["M_OUMUAMUA", 3, 20, 40, "lightRush"],
    ],
    "traits": [
        ["wideGuard", "ワイドガード", "パーティー全体の受けるダメージを軽減。重複は2体まで。"],
        ["scatter", "散弾", "通常攻撃が敵2体を自動対象にする。"],
        ["hide", "ハイド", "毎ターン30%の確率で潜伏する。"],
        ["rapid", "連射", "通常攻撃が選んだ敵へ3ヒットする。"],
        ["dash", "ダッシュ", "このキャラクターのスピードが20%上昇する。"],
        ["barrage", "弾幕", "通常攻撃が敵3体を自動対象にする。"],
        ["lightRush", "光速突進", "ターン最初の行動時、通常攻撃がSの0.5倍ダメージになる。"],
    ],
    "skills": [
        ["SK_BLACKSQUARE", "ワイドガード", "■", "味方全体の被ダメージを軽減。", "self", 0, "guard"],
        ["SK_BLACKCIRCLE", "BlackCircle", "●", "敵2体へダメージ。", "enemy", 2, "damage"],
        ["SK_HIDE", "ハイド", "◎", "このターン使用者が潜伏。", "self", 0, "hide"],
        ["SK_RAPID", "連射", "▲", "敵1体へ3回ダメージ。", "enemy", 1, "rapid"],
        ["SK_DASH", "ダッシュ", "△", "味方1体のSを3ターン上昇。", "ally", 1, "speed_buff"],
        ["SK_BARRAGE", "弾幕", "⋯", "敵3体へダメージ。", "enemy", 3, "damage"],
        ["SK_OUMUAMUA", "オウムアムア", "◉", "自分のSに応じた光速突進。", "enemy", 1, "speed_strike"],
    ],
    "skill_levels": [
        ["SK_BLACKSQUARE", 1, "", 4, "", "", .2, "", ""],
        ["SK_BLACKSQUARE", 2, "", 3, "", "", .2, "", ""],
        ["SK_BLACKSQUARE", 3, "", 2, "", "", .3, "", ""],
        ["SK_BLACKCIRCLE", 1, 7, 0, "", "", "", "", ""],
        ["SK_BLACKCIRCLE", 2, 10, 0, "", "", "", "", ""],
        ["SK_BLACKCIRCLE", 3, 14, 0, "", "", "", "", ""],
        ["SK_HIDE", 1, "", 5, "", "", "", "", ""],
        ["SK_HIDE", 2, "", 4, "", "", "", "", ""],
        ["SK_HIDE", 3, "", 3, "", "", "", "", ""],
        ["SK_RAPID", 1, "", 6, 3, .7, "", "", ""],
        ["SK_RAPID", 2, "", 5, 3, .7, "", "", ""],
        ["SK_RAPID", 3, "", 4, 3, .8, "", "", ""],
        ["SK_DASH", 1, "", 8, "", "", "", .2, 3],
        ["SK_DASH", 2, "", 7, "", "", "", .2, 3],
        ["SK_DASH", 3, "", 6, "", "", "", .3, 3],
        ["SK_BARRAGE", 1, 8, 7, "", "", "", "", ""],
        ["SK_BARRAGE", 2, 10, 6, "", "", "", "", ""],
        ["SK_BARRAGE", 3, 10, 5, "", "", "", "", ""],
        ["SK_OUMUAMUA", 1, "", 10, "", .5, "", "", ""],
        ["SK_OUMUAMUA", 2, "", 9, "", .5, "", "", ""],
        ["SK_OUMUAMUA", 3, "", 8, "", .7, "", "", ""],
    ],
    "stages": [
        ["STAGE_001", "BlackCircle", "normal", "1 WAVE / BlackCircle x1", "always", ""],
        ["STAGE_002", "Blacksquare", "normal", "2 WAVES / BlackCircle x2 / Blacksquare Lv3", "clear", "STAGE_001"],
        ["STAGE_003", "Blacksquare＆BlackCircle", "normal", "3 WAVES / Lv2-3 MIX", "clear", "STAGE_002"],
        ["STAGE_004", "hide", "normal", "1 WAVE / hider x1", "clear", "STAGE_002"],
        ["STAGE_005", "hide!!!", "normal", "3 WAVES / hider + Blacktriangle", "clear", "STAGE_004"],
        ["STAGE_006", "dash", "normal", "1 WAVE / speeder x1", "clear", "STAGE_002"],
        ["STAGE_007", "triangles", "normal", "3 WAVES / speeder + Blacktriangle", "clear", "STAGE_006"],
        ["SP_OUMUAMUA", "オウムアムア", "special", "3 WAVES / オウムアムア", "kills", "M_SPEEDER:30;M_BLACKCIRCLE:30"],
    ],
    "stage_waves": [
        ["STAGE_001", 1, 1, "M_BLACKCIRCLE", 1],
        ["STAGE_002", 1, 1, "M_BLACKCIRCLE", 1], ["STAGE_002", 1, 2, "M_BLACKCIRCLE", 1],
        ["STAGE_002", 2, 1, "M_BLACKSQUARE", 3],
        ["STAGE_003", 1, 1, "M_BLACKCIRCLE", 2], ["STAGE_003", 1, 2, "M_BLACKCIRCLE", 2], ["STAGE_003", 1, 3, "M_BLACKCIRCLE", 2],
        ["STAGE_003", 2, 1, "M_BLACKSQUARE", 2], ["STAGE_003", 2, 2, "M_BLACKSQUARE", 2], ["STAGE_003", 2, 3, "M_BLACKSQUARE", 2],
        ["STAGE_003", 3, 1, "M_BLACKSQUARE", 3], ["STAGE_003", 3, 2, "M_BLACKSQUARE", 3], ["STAGE_003", 3, 3, "M_BLACKCIRCLE", 3], ["STAGE_003", 3, 4, "M_BLACKCIRCLE", 3],
        ["STAGE_004", 1, 1, "M_HIDER", 1],
        ["STAGE_005", 1, 1, "M_HIDER", 2], ["STAGE_005", 1, 2, "M_HIDER", 2], ["STAGE_005", 1, 3, "M_HIDER", 2],
        ["STAGE_005", 2, 1, "M_BLACKTRIANGLE", 2], ["STAGE_005", 2, 2, "M_BLACKTRIANGLE", 2], ["STAGE_005", 2, 3, "M_BLACKTRIANGLE", 2],
        ["STAGE_005", 3, 1, "M_HIDER", 3], ["STAGE_005", 3, 2, "M_HIDER", 3], ["STAGE_005", 3, 3, "M_BLACKTRIANGLE", 3], ["STAGE_005", 3, 4, "M_BLACKTRIANGLE", 3],
        ["STAGE_006", 1, 1, "M_SPEEDER", 1],
        ["STAGE_007", 1, 1, "M_SPEEDER", 2], ["STAGE_007", 1, 2, "M_BLACKTRIANGLE", 2],
        ["STAGE_007", 2, 1, "M_SPEEDER", 2], ["STAGE_007", 2, 2, "M_SPEEDER", 2], ["STAGE_007", 2, 3, "M_BLACKTRIANGLE", 2], ["STAGE_007", 2, 4, "M_BLACKTRIANGLE", 2],
        ["STAGE_007", 3, 1, "M_SPEEDER", 3], ["STAGE_007", 3, 2, "M_SPEEDER", 3], ["STAGE_007", 3, 3, "M_BLACKTRIANGLE", 3], ["STAGE_007", 3, 4, "M_BLACKTRIANGLE", 3],
        ["SP_OUMUAMUA", 1, 1, "M_OUMUAMUA", 1], ["SP_OUMUAMUA", 1, 2, "M_BLACKCIRCLE", 3], ["SP_OUMUAMUA", 1, 3, "M_BLACKCIRCLE", 3],
        ["SP_OUMUAMUA", 2, 1, "M_OUMUAMUA", 2], ["SP_OUMUAMUA", 2, 2, "M_SPEEDER", 3], ["SP_OUMUAMUA", 2, 3, "M_SPEEDER", 3],
        ["SP_OUMUAMUA", 3, 1, "M_OUMUAMUA", 3],
    ],
    "drops": [
        ["M_BLACKCIRCLE", 1, "monster", "M_BLACKCIRCLE", .2],
        ["M_BLACKSQUARE", 1, "monster", "M_BLACKSQUARE", .2],
        ["M_BLACKSQUARE", 3, "skill", "SK_BLACKSQUARE", .1],
        ["M_HIDER", 1, "monster", "M_HIDER", .2],
        ["M_HIDER", 3, "skill", "SK_HIDE", .1],
        ["M_BLACKTRIANGLE", 1, "monster", "M_BLACKTRIANGLE", .2],
        ["M_BLACKTRIANGLE", 3, "skill", "SK_RAPID", .1],
        ["M_SPEEDER", 1, "monster", "M_SPEEDER", .2],
        ["M_SPEEDER", 3, "skill", "SK_DASH", .1],
        ["M_OUMUAMUA", 1, "recipe", "R_SK_BARRAGE", .1],
        ["M_OUMUAMUA", 2, "recipe", "R_SK_BARRAGE", .2],
        ["M_OUMUAMUA", 2, "recipe", "R_SK_OUMUAMUA", .1],
        ["M_OUMUAMUA", 3, "recipe", "R_SK_BARRAGE", .3],
        ["M_OUMUAMUA", 3, "recipe", "R_SK_OUMUAMUA", .2],
        ["M_OUMUAMUA", 3, "recipe", "R_M_OUMUAMUA", .2],
    ],
    "recipes": [
        ["R_SK_BARRAGE", "弾幕", "skill", "SK_BARRAGE"],
        ["R_SK_OUMUAMUA", "オウムアムア", "skill", "SK_OUMUAMUA"],
        ["R_M_OUMUAMUA", "オウムアムア", "monster", "M_OUMUAMUA"],
    ],
    "recipe_materials": [
        ["R_SK_BARRAGE", "M_BLACKCIRCLE", 5],
        ["R_SK_OUMUAMUA", "M_BLACKCIRCLE", 5],
        ["R_SK_OUMUAMUA", "M_SPEEDER", 8],
        ["R_M_OUMUAMUA", "M_BLACKCIRCLE", 10],
        ["R_M_OUMUAMUA", "M_SPEEDER", 15],
    ],
    "system_rules": [
        ["NORMAL_DAMAGE", 5, "通常攻撃の基礎ダメージ"],
        ["PARTY_SIZE", 8, "編成可能数"],
        ["FRONT_SIZE", 4, "前衛数"],
        ["MAX_LEVEL", 3, "キャラクター/スキル最大Lv"],
        ["RESERVE_TIMING", "turn_end", "撃破された前衛の交代はターン終了後"],
    ],
}


def style_sheet(ws):
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions
    fill = PatternFill("solid", fgColor="151515")
    for cell in ws[1]:
        cell.fill = fill
        cell.font = Font(color="E0FF00", bold=True)
        cell.alignment = Alignment(horizontal="center")
    for col in ws.columns:
        width = min(48, max(12, max(len(str(c.value or "")) for c in col) + 2))
        ws.column_dimensions[col[0].column_letter].width = width
    if ws.max_row > 1:
        name = "T_" + "".join(ch for ch in ws.title if ch.isalnum())[:20]
        tab = Table(displayName=name, ref=ws.dimensions)
        tab.tableStyleInfo = TableStyleInfo(
            name="TableStyleMedium2", showRowStripes=True, showFirstColumn=False
        )
        ws.add_table(tab)


def seed_workbook(path):
    if path.exists():
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        shutil.copy2(path, path.with_name(f"{path.stem}_backup_{stamp}{path.suffix}"))
    wb = Workbook()
    wb.remove(wb.active)
    readme = wb.create_sheet("README")
    readme.append(["NULL GAME DATABASE", "Excel master -> game_db.json"])
    readme.append(["更新手順", "各DBシートを編集後、tools/export_game_db.py --export-only を実行"])
    readme.append(["IDルール", "既存IDは変更しない。追加時は種別プレフィックスを使用"])
    readme.append(["注意", "stage_waves / drops / recipe_materials は複合行で管理"])
    style_sheet(readme)
    for sheet, headers in SHEETS.items():
        ws = wb.create_sheet(sheet)
        ws.append(headers)
        for row in DATA[sheet]:
            ws.append(row)
        style_sheet(ws)
    path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(path)


def rows(ws):
    headers = [c.value for c in ws[1]]
    return [
        dict(zip(headers, values))
        for values in ws.iter_rows(min_row=2, values_only=True)
        if any(v is not None for v in values)
    ]


def level_array(levels, key, default=0):
    result = [default, default, default, default]
    for row in levels:
        value = row.get(key)
        if value not in (None, ""):
            result[int(row["level"])] = value
    return result


def export_json(workbook, output):
    wb = load_workbook(workbook, data_only=True)
    data = {name: rows(wb[name]) for name in SHEETS}
    traits = {
        r["trait_id"]: {"name": r["name"], "desc": r["description"]}
        for r in data["traits"]
    }
    monsters = {}
    for r in data["characters"]:
        levels = {
            str(int(x["level"])): {
                "hp": x["hp_add"] or 0,
                "speed": x["speed_add"] or 0,
                **({"trait": x["trait_id"]} if x["trait_id"] else {}),
            }
            for x in data["character_levels"]
            if x["monster_id"] == r["monster_id"]
        }
        monsters[r["monster_id"]] = {
            "id": r["monster_id"], "name": r["name"], "glyph": r["glyph"],
            "hp": r["base_hp"], "speed": r["base_speed"], "slots": r["slots"],
            "trait": r["base_trait"] or None, "levels": levels,
            "desc": r["description"],
        }
    skills = {}
    for r in data["skills"]:
        lv = [x for x in data["skill_levels"] if x["skill_id"] == r["skill_id"]]
        item = {
            "id": r["skill_id"], "name": r["name"], "glyph": r["glyph"],
            "desc": r["description"], "target": r["target"],
        }
        if r["targets"]:
            item["targets"] = r["targets"]
        effect = r["effect_type"]
        if effect == "damage":
            item["power"] = level_array(lv, "power")
            item["ct"] = level_array(lv, "ct")
        elif effect == "guard":
            item["guardPct"] = level_array(lv, "guard_pct")
            item["ct"] = level_array(lv, "ct")
        elif effect == "hide":
            item["hide"] = True
            item["ct"] = level_array(lv, "ct")
        elif effect == "rapid":
            item["rapid"] = level_array(lv, "multiplier")
            item["hits"] = int(lv[0]["hits"])
            item["ct"] = level_array(lv, "ct")
        elif effect == "speed_buff":
            item["speedPct"] = level_array(lv, "speed_pct")
            item["ct"] = level_array(lv, "ct")
        elif effect == "speed_strike":
            item["speedStrike"] = level_array(lv, "multiplier")
            item["ct"] = level_array(lv, "ct")
        skills[r["skill_id"]] = item
    stages = {}
    for r in data["stages"]:
        wave_rows = [x for x in data["stage_waves"] if x["stage_id"] == r["stage_id"]]
        waves = []
        for wave_no in sorted({int(x["wave"]) for x in wave_rows}):
            entries = sorted(
                [x for x in wave_rows if int(x["wave"]) == wave_no],
                key=lambda x: int(x["position"]),
            )
            waves.append([
                {"id": x["monster_id"], "level": int(x["level"])}
                for x in entries
            ])
        stages[r["stage_id"]] = {
            "id": r["stage_id"], "name": r["name"], "category": r["category"],
            "info": r["info"], "waves": waves,
        }
    recipes = {}
    for r in data["recipes"]:
        req = [
            {"id": x["material_monster_id"], "count": int(x["count"])}
            for x in data["recipe_materials"]
            if x["recipe_id"] == r["recipe_id"]
        ]
        recipes[r["recipe_id"]] = {
            "id": r["recipe_id"], "name": r["name"], "kind": r["result_type"],
            "result": {"type": r["result_type"], "id": r["result_id"]},
            "requires": req,
        }
    payload = {
        "schemaVersion": 1,
        "generatedAt": datetime.now().isoformat(timespec="seconds"),
        "monsters": monsters,
        "traits": traits,
        "skills": skills,
        "stages": stages,
        "recipes": recipes,
        "drops": data["drops"],
        "systemRules": {r["rule_id"]: r["value"] for r in data["system_rules"]},
    }
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workbook", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--export-only", action="store_true")
    args = parser.parse_args()
    if not args.export_only:
        seed_workbook(args.workbook)
    export_json(args.workbook, args.output)


if __name__ == "__main__":
    main()
