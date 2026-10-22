"""Tests for the gated universe refresh (scripts/refresh_universe.py).

The failures these guard against:

* a market-cap ranking pass that runs more often than the 24 h bound of
  PROMPT.md §2.1.5 allows (each pass re-queries the provider and moves the
  floor, so a second pass inside the window is a lost refresh);
* an expansion that reorders or drops the names the universe already holds;
* a fixture re-fetch of a symbol the grid already ran, which moves the bar
  sequence and makes the stored cells stale;
* a grid expansion that recomputes or disturbs the cells that already exist.
"""
import json
from pathlib import Path

import pandas as pd
import pytest

from scripts import fetch_mcap_snapshot as fms
from scripts import refresh_universe as ru


# --------------------------------------------------------------------------
# fixtures
# --------------------------------------------------------------------------

def _entry(rank, symbol, mcap, price=1.0, reason=None):
    return {
        'rank': rank, 'symbol': symbol, 'name': symbol, 'market_cap_usd': mcap,
        'price_usd': price, 'volume_24h_usd': 0, 'kucoin_usdt_pair': True,
        'exclusion_reason': reason,
    }


def _snapshot(entries, fetched_at='2026-10-22T12:00:00+00:00', pages=10):
    return {
        'source': 'test',
        'entries': entries,
        'fetched_at': fetched_at,
        'pages_requested': pages,
        'pages_fetched': pages,
        'all_requested_pages_returned': pages == pages,
        'entries_count': len(entries),
    }


def _bars(n=200, start='2026-01-01T00:00:00+00:00', step_hours=1, price=1.0):
    idx = pd.date_range(start=start, periods=n, freq='h', tz='UTC')
    return pd.DataFrame({
        'timestamp': idx,
        'open': price,
        'high': price * 1.01,
        'low': price * 0.99,
        'close': price,
        'volume': 1000.0,
    })


@pytest.fixture()
def workspace(tmp_path, monkeypatch):
    """A small universe with one grid run, ready for the phases."""
    scan = tmp_path / 'universe' / 'last_scan.json'
    ranking = tmp_path / 'universe' / 'mcap_rank.json'
    fixtures = tmp_path / 'data' / 'fixtures'
    grid = tmp_path / 'results' / 'grid'
    scan.parent.mkdir(parents=True, exist_ok=True)
    fixtures.mkdir(parents=True, exist_ok=True)
    (grid / 'results').mkdir(parents=True, exist_ok=True)

    scan.write_text(json.dumps({
        'state': 'AWAITING_NEW_ELIGIBLE_CANDIDATES',
        'snapshot_id': 'mcap_snapshot_old',
        'snapshot_path': 'universe/mcap_snapshot_old.json',
        'scanned_at': '2026-10-21T12:00:00+00:00',
        'universe_n': 2,
        'expansion_floor': {'symbol': 'BBB/USDT', 'market_cap_usd': 1000},
        'eligible_unseen_below_floor_count': 0,
        'next_eligible_refresh_at': '2026-10-22T12:00:00+00:00',
    }))
    ranking.write_text(json.dumps({
        'updated_at': '2026-10-21T12:00:00Z',
        'snapshot_id': 'mcap_snapshot_old',
        'n_symbols': 2,
        'symbols': ['AAA/USDT', 'BBB/USDT'],
        'added_in_this_expansion': ['BBB/USDT'],
        'added_market_caps_usd': {'BBB': 1000},
    }))
    for symbol in ('AAA/USDT', 'BBB/USDT'):
        _bars(n=200).to_csv(fixtures / f"{symbol.replace('/', '_')}.csv", index=False)
    (fixtures / 'fetch_manifest.json').write_text(json.dumps([
        {'symbol': 'AAA/USDT', 'source': 'KuCoin public API /api/v1/market/candles',
         'interval': '1hour', 'timezone': 'UTC', 'rows': 200,
         'start': '2026-01-01 00:00:00+00:00', 'end': '2026-01-09 07:00:00+00:00',
         'file': 'data/fixtures/AAA_USDT.csv'},
        {'symbol': 'BBB/USDT', 'source': 'KuCoin public API /api/v1/market/candles',
         'interval': '1hour', 'timezone': 'UTC', 'rows': 200,
         'start': '2026-01-01 00:00:00+00:00', 'end': '2026-01-09 07:00:00+00:00',
         'file': 'data/fixtures/BBB_USDT.csv'},
    ]))
    for symbol in ('AAA_USDT', 'BBB_USDT'):
        for (fast, slow) in ru.GRID_PAIRS:
            cell = grid / 'results' / symbol / f'P{fast}_{slow}'
            cell.mkdir(parents=True, exist_ok=True)
            (cell / 'summary.json').write_text(json.dumps(
                {'symbol': symbol.replace('_', '/'), 'P_fast': fast, 'P_slow': slow,
                 'trade_count': 10, 'net_profit_factor': 0.5}))

    args = _Args(tmp_path, scan, ranking, fixtures, grid)
    return args


class _Args:
    def __init__(self, tmp_path, scan, ranking, fixtures, grid):
        self.scan = str(scan)
        self.ranking = str(ranking)
        self.snapshot_dir = str(tmp_path / 'universe')
        self.fixture_dir = str(fixtures)
        self.grid_run = str(grid)
        self.log = str(tmp_path / 'universe' / 'mcap_expansion_log.md')
        self.pages = 10
        self.batch_size = 10
        self.target_bars = 200
        self.min_bars = 10
        self.now = ru.parse_iso('2026-10-22T12:00:01+00:00')
        self.override_gate = False
        self.override_reason = None
        self.verification_note = None


# --------------------------------------------------------------------------
# the gate
# --------------------------------------------------------------------------

def test_gate_is_closed_before_the_recorded_bound():
    state = {'next_eligible_refresh_at': '2026-10-22T12:00:00+00:00'}
    gate = ru.gate_status(state, ru.parse_iso('2026-10-22T11:00:00+00:00'))
    assert gate['eligible'] is False
    assert 'has not elapsed' in gate['reason']


def test_gate_is_open_after_the_recorded_bound():
    state = {'next_eligible_refresh_at': '2026-10-22T12:00:00+00:00'}
    gate = ru.gate_status(state, ru.parse_iso('2026-10-22T12:00:01+00:00'))
    assert gate['eligible'] is True


def test_gate_is_open_when_the_band_was_not_exhausted():
    """No bound recorded means the ranking may be refreshed again."""
    gate = ru.gate_status({'next_eligible_refresh_at': None},
                          ru.parse_iso('2026-10-22T00:00:00+00:00'))
    assert gate['eligible'] is True


def test_fetch_refuses_before_the_bound_and_does_not_call_the_provider(workspace, monkeypatch):
    calls = []
    monkeypatch.setattr(fms, 'build_snapshot', lambda pages: calls.append(pages))
    workspace.now = ru.parse_iso('2026-10-22T11:00:00+00:00')

    with pytest.raises(SystemExit):
        ru.phase_fetch(workspace)

    assert calls == [], 'the provider must not be contacted inside the 24 h bound'


def test_fetch_override_requires_a_reason(workspace, monkeypatch):
    monkeypatch.setattr(fms, 'build_snapshot', lambda pages: pytest.fail('no provider call'))
    workspace.now = ru.parse_iso('2026-10-22T11:00:00+00:00')
    workspace.override_gate = True
    with pytest.raises(SystemExit):
        ru.phase_fetch(workspace)


def test_a_reason_alone_does_not_override_the_gate(workspace, monkeypatch):
    """The override needs both flags, so it is always a deliberate decision."""
    monkeypatch.setattr(fms, 'build_snapshot', lambda pages: pytest.fail('no provider call'))
    workspace.now = ru.parse_iso('2026-10-22T11:00:00+00:00')
    workspace.override_gate = False
    workspace.override_reason = 'because'
    with pytest.raises(SystemExit):
        ru.phase_fetch(workspace)


# --------------------------------------------------------------------------
# one pass, one snapshot, one append-only expansion
# --------------------------------------------------------------------------

def _install_snapshot(monkeypatch, snapshot):
    calls = []

    def _build(pages):
        calls.append(pages)
        return snapshot

    monkeypatch.setattr(fms, 'build_snapshot', _build)
    return calls


def test_fetch_performs_exactly_one_provider_pass(workspace, monkeypatch):
    snapshot = _snapshot([
        _entry(1, 'AAA', 5000),
        _entry(2, 'BBB', 1000),
        _entry(3, 'CCC', 900),
        _entry(4, 'DDD', 800),
    ])
    calls = _install_snapshot(monkeypatch, snapshot)

    record = ru.phase_fetch(workspace)

    assert calls == [10], 'exactly one ranking pass'
    snapshots = sorted(Path(workspace.snapshot_dir).glob('mcap_snapshot_*.json'))
    assert len(snapshots) == 1
    assert record['snapshot_path'].endswith(snapshots[0].name)
    assert record['next_eligible_refresh_at'] == '2026-10-23T12:00:00+00:00'


def test_fetch_appends_the_new_names_without_touching_the_old_ones(workspace, monkeypatch):
    snapshot = _snapshot([
        _entry(1, 'AAA', 5000),
        _entry(2, 'BBB', 1000),
        _entry(3, 'CCC', 900),
        _entry(4, 'DDD', 800),
    ])
    _install_snapshot(monkeypatch, snapshot)

    ru.phase_fetch(workspace)

    ranking = json.loads(Path(workspace.ranking).read_text())
    assert ranking['symbols'][:2] == ['AAA/USDT', 'BBB/USDT']
    assert ranking['symbols'][2:] == ['CCC/USDT', 'DDD/USDT']
    assert ranking['n_symbols'] == 4
    assert ranking['added_in_this_expansion'] == ['CCC/USDT', 'DDD/USDT']
    assert ranking['added_market_caps_usd'] == {'CCC': 900, 'DDD': 800}


def test_fetch_selects_the_batch_in_descending_market_cap_order(workspace, monkeypatch):
    snapshot = _snapshot([
        _entry(1, 'AAA', 5000),
        _entry(2, 'BBB', 1000),
        _entry(3, 'CCC', 900),
        _entry(4, 'DDD', 800),
        _entry(5, 'EEE', 700),
    ])
    _install_snapshot(monkeypatch, snapshot)
    workspace.batch_size = 2

    ru.phase_fetch(workspace)

    ranking = json.loads(Path(workspace.ranking).read_text())
    assert ranking['symbols'] == ['AAA/USDT', 'BBB/USDT', 'CCC/USDT', 'DDD/USDT']
    assert ranking['added_market_caps_usd']['CCC'] == 900
    assert ranking['added_market_caps_usd']['DDD'] == 800


def test_a_second_fetch_in_the_same_cycle_is_refused(workspace, monkeypatch):
    snapshot = _snapshot([_entry(1, 'AAA', 5000), _entry(2, 'BBB', 1000)])
    calls = _install_snapshot(monkeypatch, snapshot)

    ru.phase_fetch(workspace)
    assert len(calls) == 1

    with pytest.raises(SystemExit):
        ru.phase_fetch(workspace)
    assert len(calls) == 1, 'the second pass inside the bound must not reach the provider'


def test_fetch_keeps_the_universe_when_no_name_is_eligible(workspace, monkeypatch):
    snapshot = _snapshot([_entry(1, 'AAA', 5000), _entry(2, 'BBB', 1000),
                          _entry(3, 'CCC', 900, reason='no_tradable_kucoin_spot_usdt_pair')])
    _install_snapshot(monkeypatch, snapshot)

    record = ru.phase_fetch(workspace)

    ranking = json.loads(Path(workspace.ranking).read_text())
    assert ranking['symbols'] == ['AAA/USDT', 'BBB/USDT']
    assert record['state'] == 'AWAITING_NEW_ELIGIBLE_CANDIDATES'
    assert record['universe_n'] == 2


# --------------------------------------------------------------------------
# fixtures
# --------------------------------------------------------------------------

def test_fixture_phase_never_refetches_a_symbol_the_universe_already_holds(workspace, monkeypatch):
    requested = []

    def _fetch(symbol, target_bars):
        requested.append(symbol)
        return _bars(n=200)

    monkeypatch.setattr(ru.fk, 'fetch_full_history', _fetch)

    # a ranking with one new name, whose fixture is missing
    ranking = json.loads(Path(workspace.ranking).read_text())
    ranking['symbols'].append('CCC/USDT')
    Path(workspace.ranking).write_text(json.dumps(ranking))

    result = ru.phase_fixtures(workspace)

    assert requested == ['CCC-USDT']
    assert result['failed'] == []
    assert (Path(workspace.fixture_dir) / 'CCC_USDT.csv').exists()
    manifest = json.loads((Path(workspace.fixture_dir) / 'fetch_manifest.json').read_text())
    assert {row['symbol'] for row in manifest} == {'AAA/USDT', 'BBB/USDT', 'CCC/USDT'}


def test_fixture_phase_never_refetches_a_symbol_the_grid_already_ran(workspace, monkeypatch):
    """The bars of a gridded symbol must not be downloaded again.

    The 66 stored cells of that symbol were computed from the bars the
    universe holds; a fresh download moves the bar sequence and makes every
    one of them stale. A missing fixture of a gridded symbol is a data
    incident to restore, not a download to repeat.
    """
    requested = []

    def _fetch(symbol, target_bars):
        requested.append(symbol)
        return _bars(n=200)

    monkeypatch.setattr(ru.fk, 'fetch_full_history', _fetch)

    # AAA has its 66 cells in the workspace, but its fixture file is gone.
    (Path(workspace.fixture_dir) / 'AAA_USDT.csv').unlink()

    result = ru.phase_fixtures(workspace)

    assert requested == [], 'the bars of a gridded symbol must not be downloaded again'
    assert result['conflicts'] == ['AAA/USDT']
    assert result['failed'] == []
    # The symbol stays in the universe: it was never dropped from it.
    ranking = json.loads(Path(workspace.ranking).read_text())
    assert 'AAA/USDT' in ranking['symbols']
    state = json.loads(Path(workspace.scan).read_text())
    assert state['fixture_conflicts'] == ['AAA/USDT']


def test_fixture_validation_rejects_a_short_history():
    checks = ru.validate_fixture(_bars(n=100), snapshot_price=1.0, min_bars=17520)
    assert checks['ok'] is False
    assert checks['enough_bars'] is False


def test_fixture_validation_rejects_duplicate_timestamps():
    df = _bars(n=200)
    df.loc[5, 'timestamp'] = df.loc[4, 'timestamp']
    checks = ru.validate_fixture(df, min_bars=10)
    assert checks['duplicate_timestamps'] == 1
    assert checks['ok'] is False


def test_fixture_validation_rejects_a_gap_in_the_hourly_grid():
    df = _bars(n=200)
    df = df.drop(index=100).reset_index(drop=True)
    checks = ru.validate_fixture(df, min_bars=10)
    assert checks['non_hourly_steps'] == 1
    assert checks['ok'] is False


def test_fixture_validation_rejects_invalid_ohlc_rows():
    df = _bars(n=200)
    df.loc[7, 'high'] = df.loc[7, 'low'] * 0.5
    checks = ru.validate_fixture(df, min_bars=10)
    assert checks['invalid_ohlc_rows'] == 1
    assert checks['ok'] is False


def test_fixture_validation_checks_the_price_identity():
    ok = ru.validate_fixture(_bars(n=200, price=1.0), snapshot_price=1.05, min_bars=10)
    assert ok['price_identity_ok'] is True
    bad = ru.validate_fixture(_bars(n=200, price=1.0), snapshot_price=5.0, min_bars=10)
    assert bad['price_identity_ok'] is False
    assert bad['ok'] is False


# --------------------------------------------------------------------------
# grid expansion
# --------------------------------------------------------------------------

def test_grid_phase_uses_the_resume_path_once_per_new_symbol(workspace, monkeypatch):
    ranking = json.loads(Path(workspace.ranking).read_text())
    ranking['symbols'] += ['CCC/USDT', 'DDD/USDT']
    Path(workspace.ranking).write_text(json.dumps(ranking))
    for symbol in ('CCC/USDT', 'DDD/USDT'):
        _bars(n=200).to_csv(Path(workspace.fixture_dir) / f"{symbol.replace('/', '_')}.csv",
                             index=False)

    commands = []

    class _Result:
        returncode = 0

    def _run(cmd, check=False, cwd=None, env=None):
        commands.append(cmd)
        return _Result()

    monkeypatch.setattr(ru.subprocess, 'run', _run)

    ru.phase_grid(workspace)

    assert len(commands) == 2
    for cmd, expected_n in zip(commands, ('3', '4')):
        assert '--resume' in cmd
        assert cmd[cmd.index('--resume') + 1] == str(workspace.grid_run)
        assert cmd[cmd.index('--n') + 1] == expected_n
        assert cmd[0].endswith('python3') or cmd[0].endswith('python')


def test_grid_phase_skips_a_symbol_whose_fixture_is_missing(workspace, monkeypatch):
    """A symbol without bars cannot be gridded; it must not be run silently."""
    ranking = json.loads(Path(workspace.ranking).read_text())
    ranking['symbols'].append('CCC/USDT')
    Path(workspace.ranking).write_text(json.dumps(ranking))

    commands = []
    monkeypatch.setattr(ru.subprocess, 'run', lambda cmd, **kw: commands.append(cmd))

    result = ru.phase_grid(workspace)

    assert commands == []
    assert result['outcomes'][0]['symbol'] == 'CCC/USDT'
    assert result['outcomes'][0]['cells'] == 0


def test_grid_phase_does_not_recompute_a_symbol_that_is_already_complete(workspace, monkeypatch):
    commands = []
    monkeypatch.setattr(ru.subprocess, 'run',
                        lambda cmd, **kw: commands.append(cmd))

    ru.phase_grid(workspace)

    assert commands == []


# --------------------------------------------------------------------------
# state
# --------------------------------------------------------------------------

def test_state_phase_records_the_expansion_and_the_next_refresh(workspace, monkeypatch):
    snapshot = _snapshot([
        _entry(1, 'AAA', 5000),
        _entry(2, 'BBB', 1000),
        _entry(3, 'CCC', 900),
        # The pass reaches below the floor the batch leaves behind (900), so the
        # band below it was observed - and it is empty.
        _entry(4, 'DDD', 800, reason='no_tradable_kucoin_spot_usdt_pair'),
    ])
    snapshot_path = Path(workspace.snapshot_dir) / 'mcap_snapshot_20261022_120000.json'
    snapshot_path.write_text(json.dumps(snapshot))
    state = json.loads(Path(workspace.scan).read_text())
    state['snapshot_path'] = str(snapshot_path)
    state['snapshot_id'] = snapshot_path.stem
    state['scanned_at'] = snapshot['fetched_at']
    state['next_eligible_refresh_at'] = '2026-10-23T12:00:00+00:00'
    Path(workspace.scan).write_text(json.dumps(state))

    ranking = json.loads(Path(workspace.ranking).read_text())
    ranking['symbols'].append('CCC/USDT')
    Path(workspace.ranking).write_text(json.dumps(ranking))

    ru.phase_state(workspace)

    updated = json.loads(Path(workspace.scan).read_text())
    assert updated['universe_n'] == 3
    assert updated['state'] == 'AWAITING_NEW_ELIGIBLE_CANDIDATES'
    assert updated['eligible_unseen_below_floor_count'] == 0
    assert updated['next_eligible_refresh_at'] == '2026-10-23T12:00:00+00:00'
    assert updated['coverage_reaches_below_current_floor'] is True
    assert updated['grid_verification']['cells_expected'] == 3 * len(ru.GRID_PAIRS)


def test_state_phase_does_not_call_the_band_exhausted_when_the_pass_missed_the_new_floor(workspace):
    """A batch lowers the floor of the universe.

    A pass that stopped at the old floor never saw the band below the new one:
    the names between the two floors are exactly the ones the batch consumed.
    Such a band is not an exhausted band, and the state must not say it is.
    """
    snapshot = _snapshot([
        _entry(1, 'AAA', 5000),
        _entry(2, 'BBB', 1000),
        _entry(3, 'CCC', 900),
    ])
    snapshot_path = Path(workspace.snapshot_dir) / 'mcap_snapshot_20261022_120000.json'
    snapshot_path.write_text(json.dumps(snapshot))
    state = json.loads(Path(workspace.scan).read_text())
    state['snapshot_path'] = str(snapshot_path)
    state['scanned_at'] = snapshot['fetched_at']
    state['next_eligible_refresh_at'] = '2026-10-23T12:00:00+00:00'
    Path(workspace.scan).write_text(json.dumps(state))

    ranking = json.loads(Path(workspace.ranking).read_text())
    ranking['symbols'].append('CCC/USDT')
    Path(workspace.ranking).write_text(json.dumps(ranking))

    ru.phase_state(workspace)

    updated = json.loads(Path(workspace.scan).read_text())
    assert updated['expansion_floor']['market_cap_usd'] == 900
    assert updated['coverage_reaches_below_current_floor'] is False
    assert updated['state'] == 'INCOMPLETE_SCAN'
    # The bound of the pass is untouched: the next refresh is still due.
    assert updated['next_eligible_refresh_at'] == '2026-10-23T12:00:00+00:00'


def test_state_phase_keeps_the_expansion_state_while_names_remain(workspace):
    snapshot = _snapshot([
        _entry(1, 'AAA', 5000),
        _entry(2, 'BBB', 1000),
        _entry(3, 'CCC', 900),
        _entry(4, 'DDD', 800),
    ])
    snapshot_path = Path(workspace.snapshot_dir) / 'mcap_snapshot_20261022_120000.json'
    snapshot_path.write_text(json.dumps(snapshot))
    state = json.loads(Path(workspace.scan).read_text())
    state['snapshot_path'] = str(snapshot_path)
    Path(workspace.scan).write_text(json.dumps(state))

    ranking = json.loads(Path(workspace.ranking).read_text())
    ranking['symbols'].append('CCC/USDT')
    Path(workspace.ranking).write_text(json.dumps(ranking))

    ru.phase_state(workspace)

    updated = json.loads(Path(workspace.scan).read_text())
    assert updated['state'] == 'EXPANSION_AVAILABLE'
    assert updated['eligible_unseen_below_floor_count'] == 1
    assert updated['eligible_unseen_below_floor'][0]['symbol'] == 'DDD'


def test_state_phase_restores_a_lost_refresh_bound(workspace):
    """A record without a bound would allow a second pass inside the window."""
    snapshot = _snapshot([_entry(1, 'AAA', 5000), _entry(2, 'BBB', 1000)])
    snapshot_path = Path(workspace.snapshot_dir) / 'mcap_snapshot_20261022_120000.json'
    snapshot_path.write_text(json.dumps(snapshot))
    state = json.loads(Path(workspace.scan).read_text())
    state['snapshot_path'] = str(snapshot_path)
    state['scanned_at'] = '2026-10-22T12:00:00+00:00'
    state['next_eligible_refresh_at'] = None
    Path(workspace.scan).write_text(json.dumps(state))

    ru.phase_state(workspace)

    updated = json.loads(Path(workspace.scan).read_text())
    assert updated['next_eligible_refresh_at'] == '2026-10-23T12:00:00+00:00'


def test_state_phase_does_not_call_the_band_exhausted_when_a_probe_failed(workspace):
    """A failed history probe leaves the eligibility of that name unknown."""
    snapshot = _snapshot([_entry(1, 'AAA', 5000), _entry(2, 'BBB', 1000)])
    snapshot['history_probe_failure_count'] = 1
    snapshot['history_probe_failures'] = ['ZZZ']
    snapshot_path = Path(workspace.snapshot_dir) / 'mcap_snapshot_20261022_120000.json'
    snapshot_path.write_text(json.dumps(snapshot))
    state = json.loads(Path(workspace.scan).read_text())
    state['snapshot_path'] = str(snapshot_path)
    state['coverage_reaches_below_floor'] = True
    Path(workspace.scan).write_text(json.dumps(state))

    ru.phase_state(workspace)

    updated = json.loads(Path(workspace.scan).read_text())
    assert updated['state'] == 'INCOMPLETE_SCAN'
    assert updated['history_probe_failure_count'] == 1


# --------------------------------------------------------------------------
# one full cycle, end to end
# --------------------------------------------------------------------------

def test_one_full_cycle_expands_the_universe(workspace, monkeypatch):
    """fetch -> fixtures -> grid -> state -> log, with the providers mocked.

    The chain is what the 24 h refresh actually runs, so it is tested as a
    chain: the ranking grows append-only, every new name gets bars and 66
    cells, the scan record ends in the waiting state with a 24 h bound, and
    the expansion log carries the batch.
    """
    snapshot = _snapshot([
        _entry(1, 'AAA', 5000),
        _entry(2, 'BBB', 1000),
        _entry(3, 'CCC', 900),
        _entry(4, 'DDD', 800),
        # The pass reaches below the floor the batch leaves behind (800): the
        # band below it was observed and it is empty.
        _entry(5, 'EEE', 700, reason='no_tradable_kucoin_spot_usdt_pair'),
    ])
    _install_snapshot(monkeypatch, snapshot)
    monkeypatch.setattr(ru.fk, 'fetch_full_history',
                        lambda symbol, target_bars: _bars(n=200))

    commands = []

    def _run(cmd, check=False, cwd=None, env=None):
        """Stand in for scripts/run_grid.py --resume: write the cells."""
        commands.append(cmd)
        ranking = json.loads(Path(workspace.ranking).read_text())
        n = int(cmd[cmd.index('--n') + 1])
        symbol = ranking['symbols'][n - 1]
        for (fast, slow) in ru.GRID_PAIRS:
            cell = (Path(workspace.grid_run) / 'results'
                    / symbol.replace('/', '_') / f'P{fast}_{slow}')
            cell.mkdir(parents=True, exist_ok=True)
            (cell / 'summary.json').write_text(json.dumps(
                {'symbol': symbol, 'P_fast': fast, 'P_slow': slow,
                 'trade_count': 10, 'net_profit_factor': 0.5}))
        return None

    monkeypatch.setattr(ru.subprocess, 'run', _run)

    ru.phase_fetch(workspace)
    ru.phase_fixtures(workspace)
    ru.phase_grid(workspace)
    ru.phase_state(workspace)
    ru.phase_log(workspace)

    ranking = json.loads(Path(workspace.ranking).read_text())
    assert ranking['symbols'] == ['AAA/USDT', 'BBB/USDT', 'CCC/USDT', 'DDD/USDT']

    manifest = json.loads((Path(workspace.fixture_dir) / 'fetch_manifest.json').read_text())
    assert {row['symbol'] for row in manifest} == {
        'AAA/USDT', 'BBB/USDT', 'CCC/USDT', 'DDD/USDT'}

    assert [cmd[cmd.index('--n') + 1] for cmd in commands] == ['3', '4']

    state = json.loads(Path(workspace.scan).read_text())
    assert state['universe_n'] == 4
    assert state['state'] == 'AWAITING_NEW_ELIGIBLE_CANDIDATES'
    assert state['next_eligible_refresh_at'] == '2026-10-23T12:00:00+00:00'
    verification = state['grid_verification']
    assert verification['cells_complete'] == 4 * len(ru.GRID_PAIRS)
    assert verification['cells_expected'] == 4 * len(ru.GRID_PAIRS)
    assert verification['cells_blocked'] == 0
    assert verification['incomplete_symbols'] == []
    assert verification['symbols_without_fixture'] == []

    log = Path(workspace.log).read_text()
    assert 'N 2 -> 4' in log
    assert 'CCC/USDT' in log and 'DDD/USDT' in log


# --------------------------------------------------------------------------
# the expansion log
# --------------------------------------------------------------------------

def test_log_phase_records_a_batch_once(workspace):
    """A repeated log run must not append the same expansion twice.

    The log is the program's ordered record of every universe change
    (PROMPT.md §2.1.6); a duplicated section would make it ambiguous, and a
    session that dies between two phases has to be able to re-run the phase.
    """
    ru.phase_log(workspace)
    first = Path(workspace.log).read_text()
    ru.phase_log(workspace)
    second = Path(workspace.log).read_text()

    assert first == second, 'the log phase must be idempotent'
    assert second.count('## Batch 1 ') == 1


def test_log_phase_continues_the_batch_numbering(workspace):
    """The log numbers its sections; a new expansion continues the sequence."""
    Path(workspace.log).write_text(
        '# Market-Cap Universe Expansion Log\n\n'
        '## Batch 0 - initial program snapshot: N = 5\n\n'
        '## Batch 1 - expansion to N = 17\n\n')

    ru.phase_log(workspace)

    log = Path(workspace.log).read_text()
    assert '## Batch 2 ' in log
    assert '## Batch 1 - expansion to N = 17' in log, 'the older sections stay'
    assert 'N 1 -> 2' in log


# --------------------------------------------------------------------------
# the shared selection helpers
# --------------------------------------------------------------------------
def test_expansion_candidates_are_unseen_eligible_and_below_the_floor(tmp_path):
    snapshot = _snapshot([
        _entry(1, 'AAA', 5000),
        _entry(2, 'BBB', 1000),
        _entry(3, 'CCC', 900),
        _entry(4, 'DDD', 800, reason='no_tradable_kucoin_spot_usdt_pair'),
        _entry(5, 'EEE', 700),
    ])
    candidates = fms.select_expansion_candidates(snapshot, ['AAA/USDT', 'BBB/USDT'], 1000)
    assert [c['symbol'] for c in candidates] == ['CCC', 'EEE']


def test_expansion_floor_is_the_lowest_included_market_cap():
    floor_mcap, floor_symbol = fms.expansion_floor(
        {'AAA/USDT': 5000, 'BBB/USDT': 1000, 'CCC/USDT': None})
    assert floor_mcap == 1000
    assert floor_symbol == 'BBB/USDT'


def test_included_market_caps_resolves_an_ambiguous_ticker(tmp_path):
    """Two assets share one ticker; the fixture decides which one we hold."""
    fixtures = tmp_path / 'fixtures'
    fixtures.mkdir()
    (fixtures / 'ONE_USDT.csv').write_text('timestamp,open,high,low,close,volume\n'
                                           '2026-01-01T00:00:00+00:00,1,1,1,1,1\n')
    snapshot = _snapshot([
        _entry(1, 'ONE', 5000, price=10.0),
        _entry(2, 'ONE', 900, price=1.0),
    ])
    included = fms.included_market_caps(snapshot, ['ONE/USDT'], fixtures)
    assert included['ONE/USDT'] == 900
