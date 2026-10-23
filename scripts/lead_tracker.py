#!/usr/bin/env python3
"""Lead pipeline tracker for the LinkedIn account manager skill.

Source of truth is always a CSV file (no dependency required). `export`
additionally writes a styled .xlsx via openpyxl if it's installed; if not,
it says so and leaves the CSV as the deliverable.

Usage:
    python lead_tracker.py add    --name "Jane Doe" --source "comment on their post" \
                                   --stage cold --next-step "send connection note" \
                                   --due 2026-11-01 [--value 2000] [--notes "..."] [--file leads.csv]
    python lead_tracker.py update --name "Jane Doe" --stage call --next-step "send proposal" \
                                   --due 2026-11-05 [--file leads.csv]
    python lead_tracker.py list   [--stage warm] [--file leads.csv]
    python lead_tracker.py export [--xlsx leads.xlsx] [--file leads.csv]

Stages: cold, warm, call, proposal, won, lost
"""

import argparse
import csv
import os
import sys
from datetime import date

FIELDS = ["name", "source", "last_contact", "stage", "next_step", "due", "value", "notes"]
STAGES = {"cold", "warm", "call", "proposal", "won", "lost"}
DEFAULT_FILE = "leads.csv"


def load(path):
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def save(path, rows):
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in FIELDS})


def cmd_add(args):
    if args.stage not in STAGES:
        sys.exit(f"Unknown stage '{args.stage}'. Must be one of: {', '.join(sorted(STAGES))}")
    rows = load(args.file)
    if any(r["name"].lower() == args.name.lower() for r in rows):
        sys.exit(f"'{args.name}' already exists. Use `update` instead.")
    rows.append({
        "name": args.name,
        "source": args.source or "",
        "last_contact": args.last_contact or date.today().isoformat(),
        "stage": args.stage,
        "next_step": args.next_step or "",
        "due": args.due or "",
        "value": args.value or "",
        "notes": args.notes or "",
    })
    save(args.file, rows)
    print(f"Added '{args.name}' ({args.stage}) to {args.file}")


def cmd_update(args):
    rows = load(args.file)
    for row in rows:
        if row["name"].lower() == args.name.lower():
            if args.stage:
                if args.stage not in STAGES:
                    sys.exit(f"Unknown stage '{args.stage}'. Must be one of: {', '.join(sorted(STAGES))}")
                row["stage"] = args.stage
            if args.source:
                row["source"] = args.source
            if args.next_step:
                row["next_step"] = args.next_step
            if args.due:
                row["due"] = args.due
            if args.value:
                row["value"] = args.value
            if args.notes:
                row["notes"] = args.notes
            row["last_contact"] = args.last_contact or date.today().isoformat()
            save(args.file, rows)
            print(f"Updated '{args.name}' in {args.file}")
            return
    sys.exit(f"'{args.name}' not found in {args.file}. Use `add` instead.")


def cmd_list(args):
    rows = load(args.file)
    if args.stage:
        rows = [r for r in rows if r["stage"] == args.stage]
    if not rows:
        print("No leads found.")
        return
    widths = {f: max(len(f), *(len(r.get(f, "")) for r in rows)) for f in FIELDS}
    header = " | ".join(f.ljust(widths[f]) for f in FIELDS)
    print(header)
    print("-" * len(header))
    for row in sorted(rows, key=lambda r: (r.get("due") or "9999-99-99", r.get("name", ""))):
        print(" | ".join(row.get(f, "").ljust(widths[f]) for f in FIELDS))


def cmd_export(args):
    rows = load(args.file)
    if not rows:
        sys.exit(f"{args.file} has no leads to export.")
    try:
        from openpyxl import Workbook
        from openpyxl.styles import Font, PatternFill
    except ImportError:
        print(f"openpyxl not installed — {args.file} (CSV) is the deliverable. "
              f"Install openpyxl to also get a styled .xlsx.")
        return

    wb = Workbook()
    ws = wb.active
    ws.title = "Leads"
    ws.append(FIELDS)
    for cell in ws[1]:
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill(start_color="2563EB", end_color="2563EB", fill_type="solid")
    for row in rows:
        ws.append([row.get(f, "") for f in FIELDS])
    for col in ws.columns:
        max_len = max(len(str(c.value)) if c.value is not None else 0 for c in col)
        ws.column_dimensions[col[0].column_letter].width = max(10, max_len + 2)

    out_path = args.xlsx or os.path.splitext(args.file)[0] + ".xlsx"
    wb.save(out_path)
    print(f"Wrote {out_path} ({len(rows)} lead(s))")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--file", default=DEFAULT_FILE, help=f"CSV file to read/write (default: {DEFAULT_FILE})")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Add a new lead")
    p_add.add_argument("--name", required=True)
    p_add.add_argument("--source")
    p_add.add_argument("--stage", required=True)
    p_add.add_argument("--next-step", dest="next_step")
    p_add.add_argument("--due")
    p_add.add_argument("--value")
    p_add.add_argument("--notes")
    p_add.add_argument("--last-contact", dest="last_contact")
    p_add.set_defaults(func=cmd_add)

    p_update = sub.add_parser("update", help="Update an existing lead")
    p_update.add_argument("--name", required=True)
    p_update.add_argument("--source")
    p_update.add_argument("--stage")
    p_update.add_argument("--next-step", dest="next_step")
    p_update.add_argument("--due")
    p_update.add_argument("--value")
    p_update.add_argument("--notes")
    p_update.add_argument("--last-contact", dest="last_contact")
    p_update.set_defaults(func=cmd_update)

    p_list = sub.add_parser("list", help="List leads")
    p_list.add_argument("--stage")
    p_list.set_defaults(func=cmd_list)

    p_export = sub.add_parser("export", help="Export to .xlsx (falls back to CSV-only if openpyxl is missing)")
    p_export.add_argument("--xlsx", help="Output .xlsx path (default: same name as --file, .xlsx extension)")
    p_export.set_defaults(func=cmd_export)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
