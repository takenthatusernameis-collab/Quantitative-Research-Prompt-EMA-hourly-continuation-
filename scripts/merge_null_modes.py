#!/usr/bin/env python3
"""Merge the null modes of one null-grid-scan artifact into another.

Why this exists
---------------
The grid-wide null leg is long: over 17 556 cells it re-runs the backtest
engine for every null mode. The leg is resumable inside one artifact
directory (`scripts/null_grid_scan.py` appends to `cells.jsonl` and only
re-runs the modes a cell is still missing), but a leg that was interrupted
with a *different* `--modes` set leaves its work in a different directory:
the modes it did compute are checkpointed there, and the modes it did not
are checkpointed elsewhere.

Re-running a mode that was already computed is wasted compute - the null of a
cell is a deterministic function of the cell identity and the mode
(`null_grid_scan.cell_seed`), so the same mode computed twice gives the same
numbers. This script moves the already-computed modes into the artifact that
is being continued, so a continued pass only computes what is genuinely
missing.

The merge is strict: a mode that exists in both artifacts must agree
exactly, cell by cell. A disagreement means the two artifacts are not
comparable (different window, costs or fixture set), and the merge refuses
rather than silently picking one of the two values.

Usage:
    python scripts/merge_null_modes.py --target results/20261021_073300_null_grid_scan \\
        --source results/20261021_035000_null_grid_scan --modes timing
"""
import argparse
import json
from pathlib import Path


def cell_key(row: dict) -> tuple:
    """The identity of a grid cell."""
    return (row['symbol'], int(row['P_fast']), int(row['P_slow']))


def read_checkpoint(path: Path) -> dict:
    """Read a `cells.jsonl` checkpoint into a cell-keyed dict.

    A checkpoint written by a pass that was killed mid-write can end in a
    truncated line. Such a line is dropped: the cell it belongs to is simply
    not merged, and the pass that continues the leg computes it again.
    """
    rows = {}
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            rows[cell_key(row)] = row
    return rows


def merge_rows(target: dict, source: dict, modes: list) -> dict:
    """Merge the requested modes of `source` into `target`.

    Returns a report with the cells that were added, the modes that were
    copied, the cells that were already complete and the conflicts that
    stopped the merge.
    """
    added = []
    copied = {}
    already = []
    conflicts = []
    for key, source_row in source.items():
        target_row = target.get(key)
        if target_row is None:
            target_row = json.loads(json.dumps(source_row, default=str))
            target[key] = target_row
            added.append(key)
        target_null = target_row.setdefault('null', {})
        for mode in modes:
            source_stats = (source_row.get('null') or {}).get(mode)
            if source_stats is None:
                continue
            existing = target_null.get(mode)
            if existing is None:
                target_null[mode] = source_stats
                copied.setdefault(mode, []).append(key)
            elif existing == source_stats:
                already.append((key, mode))
            else:
                conflicts.append((key, mode))
    return {
        'added_cells': added,
        'copied_modes': copied,
        'already_present': already,
        'conflicts': conflicts,
    }


def write_checkpoint(path: Path, rows: dict) -> None:
    """Write the merged checkpoint, one row per cell, in a stable order."""
    tmp = path.with_name(path.name + '.tmp')
    with open(tmp, 'w') as fh:
        for key in sorted(rows):
            fh.write(json.dumps(rows[key], default=str) + '\n')
    tmp.replace(path)


def main() -> None:
    parser = argparse.ArgumentParser(
        description='Merge the null modes of one null-grid-scan artifact into another')
    parser.add_argument('--target', required=True,
                        help='results/<TS>_null_grid_scan directory that is continued')
    parser.add_argument('--source', required=True,
                        help='results/<TS>_null_grid_scan directory the modes come from')
    parser.add_argument('--modes', nargs='*', default=None,
                        help='Modes to take from the source (default: every mode the '
                             'source has that the target is missing)')
    parser.add_argument('--dry-run', action='store_true',
                        help='Report the merge without writing it')
    args = parser.parse_args()

    target_dir = Path(args.target)
    source_dir = Path(args.source)
    target_path = target_dir / 'cells.jsonl'
    source_path = source_dir / 'cells.jsonl'
    for path in (target_path, source_path):
        if not path.exists():
            raise SystemExit(f'no cells.jsonl in {path.parent}')

    target = read_checkpoint(target_path)
    source = read_checkpoint(source_path)

    if args.modes:
        modes = list(args.modes)
    else:
        source_modes = set()
        for row in source.values():
            source_modes |= set(row.get('null') or {})
        target_modes = set()
        for row in target.values():
            target_modes |= set(row.get('null') or {})
        modes = sorted(source_modes - target_modes) or sorted(source_modes)

    report = merge_rows(target, source, modes)
    if report['conflicts']:
        sample = report['conflicts'][:5]
        raise SystemExit(
            f'{len(report["conflicts"])} cells disagree between the two artifacts '
            f'(e.g. {sample}). The artifacts are not comparable; merge aborted.')

    total_copied = sum(len(v) for v in report['copied_modes'].values())
    print(f'Target {target_dir}: {len(target)} cells')
    print(f'Source {source_dir}: {len(source)} cells')
    print(f'Modes merged: {modes}')
    for mode, keys in sorted(report['copied_modes'].items()):
        print(f'  {mode}: copied into {len(keys)} cells')
    print(f'Cells added from the source: {len(report["added_cells"])}')
    print(f'Cells that already held the mode: {len(report["already_present"])}')
    if args.dry_run:
        print('Dry run: nothing written')
        return
    write_checkpoint(target_path, target)
    print(f'Wrote {target_path} ({len(target)} cells)')


if __name__ == '__main__':
    main()
