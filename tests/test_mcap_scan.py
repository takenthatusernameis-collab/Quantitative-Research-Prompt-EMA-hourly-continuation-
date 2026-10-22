"""Tests for the market-cap ranking scan, its coverage record and the scan state.

The failure these guard against is a ranking pass that stops above the current
expansion floor being reported as "no eligible names left": such a pass never
looked at the band the expansion works on.
"""
from pathlib import Path

import pytest

from scripts import fetch_mcap_snapshot as fms


def _entry(rank, symbol, mcap, reason=None):
    return {
        'rank': rank, 'symbol': symbol, 'name': symbol, 'market_cap_usd': mcap,
        'price_usd': 1.0, 'volume_24h_usd': 0, 'kucoin_usdt_pair': True,
        'exclusion_reason': reason,
    }


def _snapshot(entries, pages_requested=None, pages_fetched=None):
    snap = {
        'source': 'test',
        'entries': entries,
        'fetched_at': '2026-10-20T10:00:00+00:00',
    }
    if pages_requested is not None:
        snap['pages_requested'] = pages_requested
    if pages_fetched is not None:
        snap['pages_fetched'] = pages_fetched
    return snap


def test_coverage_facts_derived_from_entries():
    """Legacy snapshots without coverage fields still report their real coverage."""
    snap = _snapshot([_entry(1, 'AAA', 900), _entry(2, 'BBB', 500)], pages_fetched=2)
    facts = fms.coverage_facts(snap)
    assert facts['entries_count'] == 2
    assert facts['lowest_rank_covered'] == 2
    assert facts['lowest_market_cap_usd'] == 500
    assert facts['all_requested_pages_returned'] is True


def test_coverage_stops_above_floor_is_not_complete_for_the_band():
    """A pass that ends above the floor cannot answer the eligibility question."""
    snap = _snapshot([_entry(500, 'QQQX', 45_076_197)], pages_requested=5, pages_fetched=5)
    assert fms.coverage_reaches_below_floor(snap, 41_203_035) is False


def test_coverage_that_reaches_below_floor_is_complete_for_the_band():
    snap = _snapshot([_entry(1000, 'OLAS', 15_182_785)], pages_requested=10, pages_fetched=10)
    assert fms.coverage_reaches_below_floor(snap, 41_203_035) is True


def test_coverage_with_no_entries_is_never_complete():
    assert fms.coverage_reaches_below_floor(_snapshot([]), 41_203_035) is False


def test_scan_record_reports_expansion_available_when_names_exist():
    """Eligible unseen names below the floor mean the program must expand."""
    snap = _snapshot([_entry(539, 'CCD', 41_018_152)], pages_requested=10, pages_fetched=10)
    record = fms.build_scan_record(
        snap, Path('universe/mcap_snapshot_x.json'), ['BOME/USDT'], 41_203_035,
        'BOME/USDT', [_entry(539, 'CCD', 41_018_152)], [], snap['fetched_at'])
    assert record['state'] == 'EXPANSION_AVAILABLE'
    assert record['eligible_unseen_below_floor_count'] == 1
    assert record['coverage_reaches_below_floor'] is True
    assert record['next_eligible_refresh_at'] is None


def test_scan_record_waits_24h_after_a_complete_but_empty_pass():
    """A complete pass with nothing to add is a waiting state, not a stop."""
    snap = _snapshot([_entry(1000, 'OLAS', 15_182_785)], pages_requested=10, pages_fetched=10)
    record = fms.build_scan_record(
        snap, Path('universe/mcap_snapshot_x.json'), ['BOME/USDT'], 41_203_035,
        'BOME/USDT', [], [], snap['fetched_at'])
    assert record['state'] == 'AWAITING_NEW_ELIGIBLE_CANDIDATES'
    assert record['next_eligible_refresh_at'] == '2026-10-21T10:00:00+00:00'


def test_scan_record_marks_a_truncated_pass_as_incomplete():
    """The 5-page pass of 2026-10-20T10:02:36Z stopped above the floor."""
    snap = _snapshot([_entry(500, 'QQQX', 45_076_197)], pages_requested=5, pages_fetched=5)
    record = fms.build_scan_record(
        snap, Path('universe/mcap_snapshot_x.json'), ['BOME/USDT'], 41_203_035,
        'BOME/USDT', [], [], snap['fetched_at'])
    assert record['state'] == 'INCOMPLETE_SCAN'
    assert record['coverage_reaches_below_floor'] is False
    assert record['next_eligible_refresh_at'] is not None


def test_build_snapshot_records_the_pages_that_actually_returned(monkeypatch):
    """A pass that stops early must not claim the requested coverage."""
    rows = [{'symbol': 'aaa', 'name': 'AAA', 'market_cap': 1000,
             'current_price': 1.0, 'total_volume': 0}]
    monkeypatch.setattr(fms, 'fetch_markets', lambda pages: (rows, 1))
    monkeypatch.setattr(fms, 'fetch_kucoin_usdt_pairs', lambda: {'AAA'})
    monkeypatch.setattr(fms, 'price_identity_ok', lambda entry: True)
    monkeypatch.setattr(fms, 'has_min_history', lambda symbol: True)

    snap = fms.build_snapshot(10)
    assert snap['pages_requested'] == 10
    assert snap['pages_fetched'] == 1
    assert snap['all_requested_pages_returned'] is False
    assert snap['entries_count'] == 1
    assert snap['lowest_market_cap_usd'] == 1000


# --------------------------------------------------------------------------
# a failed probe is unknown, not a rejection
# --------------------------------------------------------------------------

def test_history_probe_failure_does_not_exclude_a_name(monkeypatch):
    """PROMPT.md §2.1.5: an API failure is not proof of ineligibility."""
    rows = [{'symbol': 'aaa', 'name': 'AAA', 'market_cap': 1000,
             'current_price': 1.0, 'total_volume': 0}]
    monkeypatch.setattr(fms, 'fetch_markets', lambda pages: (rows, 1))
    monkeypatch.setattr(fms, 'fetch_kucoin_usdt_pairs', lambda: {'AAA'})
    monkeypatch.setattr(fms, 'price_identity_ok', lambda entry: True)
    monkeypatch.setattr(fms, 'has_min_history', lambda symbol: None)

    snap = fms.build_snapshot(10)

    assert snap['entries'][0]['exclusion_reason'] is None
    assert snap['entries'][0]['history_probe_failed'] is True
    assert snap['history_probe_failures'] == ['AAA']
    assert snap['history_probe_failure_count'] == 1


def test_history_probe_failure_keeps_the_name_a_candidate(monkeypatch):
    """The name stays selectable; the fixture download is the real gate."""
    rows = [{'symbol': 'aaa', 'name': 'AAA', 'market_cap': 1000,
             'current_price': 1.0, 'total_volume': 0}]
    monkeypatch.setattr(fms, 'fetch_markets', lambda pages: (rows, 1))
    monkeypatch.setattr(fms, 'fetch_kucoin_usdt_pairs', lambda: {'AAA'})
    monkeypatch.setattr(fms, 'price_identity_ok', lambda entry: True)
    monkeypatch.setattr(fms, 'has_min_history', lambda symbol: None)

    snap = fms.build_snapshot(10)

    candidates = fms.select_expansion_candidates(snap, ['BBB/USDT'], 2000)
    assert [c['symbol'] for c in candidates] == ['AAA']


def test_a_name_without_history_is_still_excluded(monkeypatch):
    rows = [{'symbol': 'aaa', 'name': 'AAA', 'market_cap': 1000,
             'current_price': 1.0, 'total_volume': 0}]
    monkeypatch.setattr(fms, 'fetch_markets', lambda pages: (rows, 1))
    monkeypatch.setattr(fms, 'fetch_kucoin_usdt_pairs', lambda: {'AAA'})
    monkeypatch.setattr(fms, 'price_identity_ok', lambda entry: True)
    monkeypatch.setattr(fms, 'has_min_history', lambda symbol: False)

    snap = fms.build_snapshot(10)

    assert snap['entries'][0]['exclusion_reason'] == 'insufficient_hourly_history_for_grid'
    assert snap['history_probe_failure_count'] == 0


def test_has_min_history_reports_a_failed_probe_as_unknown(monkeypatch):
    """The probe answers True/False/None - a failed call is not "no history"."""

    class _Boom:
        @staticmethod
        def json():
            raise ValueError('no json')

    monkeypatch.setattr(fms, 'get_with_retry', lambda *a, **kw: _Boom())
    assert fms.has_min_history('AAA') is None


def test_has_min_history_reports_an_error_answer_as_unknown(monkeypatch):
    """KuCoin's transient 400100 (batch 12) says nothing about the listing."""

    class _Err:
        @staticmethod
        def json():
            return {'code': '400100', 'data': []}

    monkeypatch.setattr(fms, 'get_with_retry', lambda *a, **kw: _Err())
    assert fms.has_min_history('AAA') is None


def test_has_min_history_reports_a_missing_bar_series_as_no_history(monkeypatch):
    class _Empty:
        @staticmethod
        def json():
            return {'code': '200000', 'data': []}

    monkeypatch.setattr(fms, 'get_with_retry', lambda *a, **kw: _Empty())
    assert fms.has_min_history('AAA') is False
