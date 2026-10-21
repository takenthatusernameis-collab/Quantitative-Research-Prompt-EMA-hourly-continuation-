"""Tests for the null-mode merge (scripts/merge_null_modes.py)."""
import json
import subprocess
import sys
from pathlib import Path

import pytest

from scripts.merge_null_modes import (cell_key, merge_rows, read_checkpoint,
                                      write_checkpoint)


def _row(symbol, fast, slow, null):
    return {'symbol': symbol, 'P_fast': fast, 'P_slow': slow,
            'real': {'net_pf': 0.5}, 'null': null}


def test_cell_key_identifies_a_grid_cell():
    assert cell_key(_row('ADA/USDT', 8, 20, {})) == ('ADA/USDT', 8, 20)


def test_merge_copies_a_missing_mode_into_the_target():
    """The mode the source computed is moved into the artifact being continued."""
    target = {('ADA/USDT', 8, 20): _row('ADA/USDT', 8, 20, {'block': {'net_pf': 0.4}})}
    source = {('ADA/USDT', 8, 20): _row('ADA/USDT', 8, 20,
                                        {'block': {'net_pf': 0.4}, 'timing': {'net_pf': 0.6}})}
    report = merge_rows(target, source, ['timing'])
    assert report['conflicts'] == []
    assert report['copied_modes']['timing'] == [('ADA/USDT', 8, 20)]
    assert target[('ADA/USDT', 8, 20)]['null']['timing'] == {'net_pf': 0.6}
    # The mode the target already had is untouched.
    assert target[('ADA/USDT', 8, 20)]['null']['block'] == {'net_pf': 0.4}


def test_merge_adds_a_cell_the_target_does_not_hold_yet():
    """A cell the source covers and the target does not is carried over."""
    target = {}
    source = {('BTC/USDT', 50, 100): _row('BTC/USDT', 50, 100, {'timing': {'net_pf': 0.7}})}
    report = merge_rows(target, source, ['timing'])
    assert report['added_cells'] == [('BTC/USDT', 50, 100)]
    assert target[('BTC/USDT', 50, 100)]['null']['timing'] == {'net_pf': 0.7}


def test_merge_reports_a_conflict_instead_of_overwriting_it():
    """Two artifacts that disagree are not comparable, so the merge refuses."""
    target = {('ADA/USDT', 8, 20): _row('ADA/USDT', 8, 20, {'timing': {'net_pf': 0.4}})}
    source = {('ADA/USDT', 8, 20): _row('ADA/USDT', 8, 20, {'timing': {'net_pf': 0.6}})}
    report = merge_rows(target, source, ['timing'])
    assert report['conflicts'] == [(('ADA/USDT', 8, 20), 'timing')]
    # The value that was already there is not silently replaced.
    assert target[('ADA/USDT', 8, 20)]['null']['timing'] == {'net_pf': 0.4}


def test_checkpoint_round_trip_keeps_one_row_per_cell():
    """The merged checkpoint is written once per cell, in a stable order."""
    path = Path('results') / '_merge_test_cells.jsonl'
    try:
        rows = {('B/USDT', 8, 20): _row('B/USDT', 8, 20, {'timing': {'net_pf': 0.1}}),
                ('A/USDT', 50, 100): _row('A/USDT', 50, 100, {'timing': {'net_pf': 0.2}})}
        write_checkpoint(path, rows)
        back = read_checkpoint(path)
        assert set(back) == set(rows)
        assert [cell_key(json.loads(line)) for line in
                path.read_text().splitlines() if line.strip()] == \
            [('A/USDT', 50, 100), ('B/USDT', 8, 20)]
    finally:
        path.unlink(missing_ok=True)


def test_the_cli_aborts_on_a_conflict(tmp_path):
    """The command line path refuses a merge that would hide a disagreement."""
    source = tmp_path / 'source'
    target = tmp_path / 'target'
    source.mkdir()
    target.mkdir()
    (source / 'cells.jsonl').write_text(json.dumps(
        _row('ADA/USDT', 8, 20, {'timing': {'net_pf': 0.6}})) + '\n')
    (target / 'cells.jsonl').write_text(json.dumps(
        _row('ADA/USDT', 8, 20, {'timing': {'net_pf': 0.4}})) + '\n')
    result = subprocess.run(
        [sys.executable, '-m', 'scripts.merge_null_modes',
         '--target', str(target), '--source', str(source), '--modes', 'timing'],
        capture_output=True, text=True)
    assert result.returncode != 0
    assert 'not comparable' in (result.stdout + result.stderr)


def test_the_cli_merges_and_writes_the_target(tmp_path):
    """The command line path writes the merged checkpoint."""
    source = tmp_path / 'source'
    target = tmp_path / 'target'
    source.mkdir()
    target.mkdir()
    (source / 'cells.jsonl').write_text(json.dumps(
        _row('ADA/USDT', 8, 20, {'timing': {'net_pf': 0.6}})) + '\n')
    (target / 'cells.jsonl').write_text(json.dumps(
        _row('ADA/USDT', 8, 20, {'block': {'net_pf': 0.4}})) + '\n')
    result = subprocess.run(
        [sys.executable, '-m', 'scripts.merge_null_modes',
         '--target', str(target), '--source', str(source), '--modes', 'timing'],
        capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    merged = read_checkpoint(target / 'cells.jsonl')
    assert set(merged[('ADA/USDT', 8, 20)]['null']) == {'block', 'timing'}
