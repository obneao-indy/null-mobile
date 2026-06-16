import argparse
import json
import re
from datetime import datetime
from pathlib import Path


SECTIONS = {
    "characters": ("monsters", "Characters", "character"),
    "traits": ("traits", "Traits", "trait"),
    "skills": ("skills", "Skills", "skill"),
    "stages": ("stages", "Stages", "stage"),
    "recipes": ("recipes", "Recipes", "recipe"),
}


def safe_name(value):
    return re.sub(r'[<>:"/\\|?*]', "_", value).strip().rstrip(".")


def note_text(kind, item):
    name = item.get("name", item["id"])
    lines = [
        "---",
        f"type: null-{kind}",
        f"id: {item['id']}",
        f"name: {name}",
        "---",
        "",
        f"# {name}",
        "",
    ]
    if item.get("desc"):
        lines.extend([item["desc"], ""])
    visual = item.get("visual", {})
    vault_src = visual.get("vaultSrc")
    if vault_src:
        lines.extend(["## Visual", "", f"![[{vault_src}]]", ""])
    lines.extend([
        "## Data",
        "",
        "このJSONブロックがゲームDBへ出力されます。キー名は変更せず、値を編集してください。",
        "",
        "```json",
        json.dumps(item, ensure_ascii=False, indent=2),
        "```",
        "",
    ])
    return "\n".join(lines)


def data_note(title, data):
    return "\n".join([
        "---",
        "type: null-data",
        f"name: {title}",
        "---",
        "",
        f"# {title}",
        "",
        "```json",
        json.dumps(data, ensure_ascii=False, indent=2),
        "```",
        "",
    ])


def extract_json(path):
    text = path.read_text(encoding="utf-8")
    match = re.search(r"```json\s*(.*?)\s*```", text, re.DOTALL)
    if not match:
        raise ValueError(f"JSON block not found: {path}")
    return json.loads(match.group(1))


def init_vault(source, vault):
    payload = json.loads(source.read_text(encoding="utf-8"))
    vault.mkdir(parents=True, exist_ok=True)
    links = ["# NULL GAME DB", "", "ObsidianでこのフォルダをVaultとして開けます。", ""]
    for _, (json_key, folder_name, kind) in SECTIONS.items():
        folder = vault / folder_name
        folder.mkdir(exist_ok=True)
        links.extend([f"## {folder_name}", ""])
        for item_id, item in payload.get(json_key, {}).items():
            item = {"id": item_id, **item}
            file_name = safe_name(f"{item_id} {item.get('name', '')}") + ".md"
            (folder / file_name).write_text(note_text(kind, item), encoding="utf-8")
            links.append(f"- [[{folder_name}/{file_name[:-3]}|{item.get('name', item_id)}]]")
        links.append("")
    data_dir = vault / "Data"
    data_dir.mkdir(exist_ok=True)
    (data_dir / "Drops.md").write_text(data_note("Drops", payload.get("drops", [])), encoding="utf-8")
    (data_dir / "System Rules.md").write_text(
        data_note("System Rules", payload.get("systemRules", {})), encoding="utf-8"
    )
    links.extend([
        "## Data",
        "",
        "- [[Data/Drops]]",
        "- [[Data/System Rules]]",
        "",
        "## Export",
        "",
        "```powershell",
        "python tools/markdown_game_db.py export --vault NULL_GAME_DB --output game_db.json",
        "```",
        "",
    ])
    (vault / "README.md").write_text("\n".join(links), encoding="utf-8")


def export_vault(vault, output):
    payload = {
        "schemaVersion": 1,
        "generatedAt": datetime.now().isoformat(timespec="seconds"),
    }
    for _, (json_key, folder_name, _) in SECTIONS.items():
        entries = {}
        for path in sorted((vault / folder_name).glob("*.md")):
            item = extract_json(path)
            entries[item["id"]] = item
        payload[json_key] = entries
    payload["drops"] = extract_json(vault / "Data" / "Drops.md")
    payload["systemRules"] = extract_json(vault / "Data" / "System Rules.md")
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Convert NULL's Obsidian Markdown DB.")
    sub = parser.add_subparsers(dest="command", required=True)
    init = sub.add_parser("init", help="Create an Obsidian vault from game_db.json.")
    init.add_argument("--source", type=Path, default=Path("game_db.json"))
    init.add_argument("--vault", type=Path, default=Path("NULL_GAME_DB"))
    export = sub.add_parser("export", help="Export the Obsidian vault to game_db.json.")
    export.add_argument("--vault", type=Path, default=Path("NULL_GAME_DB"))
    export.add_argument("--output", type=Path, default=Path("game_db.json"))
    args = parser.parse_args()
    if args.command == "init":
        init_vault(args.source, args.vault)
    else:
        export_vault(args.vault, args.output)


if __name__ == "__main__":
    main()
