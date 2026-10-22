"""Tests for the 24 h refresh bound of the market-cap ranking.

The failures these guard against:

* a ranking pass that runs before the recorded bound has elapsed - every pass
  re-queries the provider and moves the expansion floor, so a second pass
  inside the window is a lost refresh and a broken PROMPT.md §2.1.5 rule;
* a scan record that *loses* its bound. A record without a bound reads as
  "the gate is open", so a pass that finds eligible names (the state
  `EXPANSION_AVAILABLE`) used to open the gate for an unlimited number of
  further passes;
* the two tools that can query the provider - the gated entry point
  (`scripts/refresh_universe.py`) and the classic path
  (`scripts/fetch_mcap_snapshot.py`) - disagreeing about the bound.
"""
import json
import sys
from datetime import datetime, timezone

import pytest

from scripts import fetch_mcap_snapshot as fms
from scripts import refresh_gate as gate
from scripts import refresh_universe as ru


# A bound in the far past: the gate is open, whatever the wall clock says.
OPEN_BOUND = '2020-01-01T00:00:00+00:00'
# A bound in the far future: the gate is closed, whatever the wall clock says.
CLOSED_BOUND = '2099-01-01T00:00:00+00:00'


def _entry(rank, symbol, mcap, reason=None):
    return {
        'rank': rank, 'symbol': symbol, 'name': symbol, 'market_cap_usd': mcap,
        'price_usd': 1.0, 'volume_24h_usd': 0, 'kucoin_usdt_pair': True,
        'exclusion_reason': reason,
    }


def _snapshot(entries, fetched_at='2026-10-22T12:00:00+00:00'):
    return {
        'source': 'test',
        'entries': entries,
        'fetched_at': fetched_at,
        'pages_requested': 10,
        'pages_fetched': 10,
        'all_requested_pages_returned': True,
        'entries_count': len(entries),
    }


@pytest.fixture()
def workspace(tmp_path, monkeypatch):
    """A small universe whose scan record carries a chosen bound."""
    out_dir = tmp_path / 'universe'
    out_dir.mkdir(parents=True, exist_ok=True)
    (tmp_path / 'data' / 'fixtures').mkdir(parents=True, exist_ok=True)
    ranking = out_dir / 'mcap_rank.json'
    ranking.write_text(json.dumps({
        'updated_at': '2026-10-21T12:00:00Z',
        'snapshot_id': 'mcap_snapshot_old',
        'n_symbols': 1,
        'symbols': ['AAA/USDT'],
        'added_in_this_expansion': ['AAA/USDT'],
        'added_market_caps_usd': {'AAA': 5000},
    }))
    state = {'out_dir': out_dir, 'ranking': ranking,
             'scan': out_dir / 'last_scan.json'}

    def _write_bound(bound):
        state['scan'].write_text(json.dumps({
            'state': 'AWAITING_NEW_ELIGIBLE_CANDIDATES',
            'scanned_at': '2026-10-21T12:00:00+00:00',
            'universe_n': 1,
            'next_eligible_refresh_at': bound,
        }))

    state['write_bound'] = _write_bound
    _write_bound(OPEN_BOUND)

    def _run(*argv):
        monkeypatch.setattr(sys, 'argv', ['fetch_mcap_snapshot.py', *argv])
        fms.main()

    state['run'] = _run
    return state


def _install_snapshot(monkeypatch, snapshot):
    calls = []

    def _build(pages):
        calls.append(pages)
        return snapshot

    monkeypatch.setattr(fms, 'build_snapshot', _build)
    return calls


# --------------------------------------------------------------------------
# one source of truth for the bound
# --------------------------------------------------------------------------

def test_both_tools_use_the_same_gate_logic():
    """The gated entry point and the classic path must not drift apart."""
    assert ru.gate_status is gate.gate_status
    assert ru.require_open_gate is gate.require_open_gate
    assert ru.override_reason is gate.override_reason
    assert ru.parse_iso is gate.parse_iso


def test_the_bound_is_the_pass_time_plus_24h():
    assert gate.bound_after('2026-10-22T12:00:00+00:00') == '2026-10-23T12:00:00+00:00'


def test_the_bound_of_a_pass_ignores_when_the_batch_is_applied():
    """Applying a frozen snapshot does not move the bound of its pass."""
    pass_time = '2026-10-22T12:00:00+00:00'
    assert gate.bound_after(pass_time) == '2026-10-23T12:00:00+00:00'
    # The bound follows the pass, not the moment the batch is applied.
    assert gate.bound_after(pass_time) != gate.bound_after(
        datetime.now(timezone.utc).isoformat())


# --------------------------------------------------------------------------
# the classic path obeys the bound
# --------------------------------------------------------------------------

def test_the_classic_path_refuses_a_pass_before_the_bound(workspace, monkeypatch):
    workspace['write_bound'](CLOSED_BOUND)
    calls = _install_snapshot(monkeypatch, _snapshot([_entry(1, 'AAA', 5000)]))

    with pytest.raises(SystemExit):
        workspace['run']('--pages', '20', '--out-dir', str(workspace['out_dir']),
                         '--mcap', str(workspace['ranking']))

    assert calls == [], 'the provider must not be contacted inside the 24 h bound'


def test_the_classic_path_allows_a_deliberate_override(workspace, monkeypatch):
    workspace['write_bound'](CLOSED_BOUND)
    calls = _install_snapshot(monkeypatch, _snapshot([_entry(1, 'AAA', 5000)]))

    workspace['run']('--pages', '20', '--out-dir', str(workspace['out_dir']),
                     '--mcap', str(workspace['ranking']),
                     '--override-gate', '--override-reason', 'history probes failed')

    assert calls == [20]


def test_a_reason_alone_does_not_override_the_bound(workspace, monkeypatch):
    workspace['write_bound'](CLOSED_BOUND)
    calls = _install_snapshot(monkeypatch, _snapshot([_entry(1, 'AAA', 5000)]))

    with pytest.raises(SystemExit):
        workspace['run']('--pages', '20', '--out-dir', str(workspace['out_dir']),
                         '--mcap', str(workspace['ranking']),
                         '--override-reason', 'history probes failed')

    assert calls == []


def test_the_classic_path_records_the_bound_even_when_names_are_eligible(workspace, monkeypatch):
    """A pass that finds names must not leave the gate open for another one."""
    _install_snapshot(monkeypatch, _snapshot([
        _entry(1, 'AAA', 5000),
        _entry(2, 'BBB', 900),
    ]))

    workspace['run']('--pages', '20', '--out-dir', str(workspace['out_dir']),
                     '--mcap', str(workspace['ranking']))

    record = json.loads(workspace['scan'].read_text())
    assert record['state'] == 'EXPANSION_AVAILABLE'
    assert record['next_eligible_refresh_at'] == '2026-10-23T12:00:00+00:00'
    assert gate.gate_status(record)['eligible'] is False


def test_applying_a_frozen_snapshot_is_not_gated(workspace, monkeypatch):
    """Applying a frozen snapshot makes no provider call, so it is not gated."""
    workspace['write_bound'](CLOSED_BOUND)
    calls = _install_snapshot(monkeypatch, _snapshot([_entry(1, 'AAA', 5000)]))
    frozen = workspace['out_dir'] / 'mcap_snapshot_20261022_120000.json'
    frozen.write_text(json.dumps(_snapshot([
        _entry(1, 'AAA', 5000),
        _entry(2, 'BBB', 900),
    ])))

    workspace['run']('--apply-from', str(frozen),
                     '--out-dir', str(workspace['out_dir']),
                     '--mcap', str(workspace['ranking']))

    assert calls == [], 'applying a frozen snapshot must not query the provider'
    record = json.loads(workspace['scan'].read_text())
    # The bound still belongs to the pass that produced the snapshot.
    assert record['next_eligible_refresh_at'] == '2026-10-23T12:00:00+00:00'
