# NEXT TASK — refresh bound 2026-10-24T12:28:28.949476Z

## Update 2026-10-23T19:40 UTC (current session)

Offline verification completed (no provider contact).
- `PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"` → `{'eligible': False, 'bound': '2026-10-24T12:28:28.949476+00:00', 'now': '2026-10-23T19:43:52+00:00', 'reason': 'the 24 h refresh bound 2026-10-24T12:28:28.949476+00:00 has not elapsed yet'}`
- `universe/last_scan.json`: `state=AWAITING_NEW_ELIGIBLE_CANDIDATES`, `universe_n=275`, `snapshot_id=mcap_snapshot_20261023_122828`, `scanned_at=2026-10-23T12:28:28.949476+00:00`, 20 pages/2000 entries, lowest $3,441,774, `expansion_floor=BOSON/USDT $3,558,643`, `eligible_unseen_below_floor_count=0`, `batch_selected=[]`, `next_eligible_refresh_at=2026-10-24T12:28:28.949476+00:00`
- `results/20261019_135940_grid`: complete (18150/18150), 0 credible candidates. `results/mutations.json`: C_stricter_trend/C_min_risk_atr NOT_PROMOTED.
- `results/20261023_050716_null_grid_scan/`: no edge.

**Your job:** wait until 2026-10-24T12:28:28.949476Z, then execute the refresh cycle. Do not contact CoinGecko/KuCoin before that timestamp.

## Your task (in order)

1. **Verify eligibility offline:** `PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"` → must return `eligible: True`.
2. **Run exactly one 20-page pass:** `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20`
3. **Freeze snapshot for 24h** (writes bound to `universe/last_scan.json`).
4. **Re-check band below current floor** for eligible unseen candidates.
5. **If candidates exist:** expand per PROMPT.md §2.1 (append descending, log to `universe/mcap_expansion_log.md`, fetch OHLCV via `scripts/fetch_kucoin.py`, run full 66-pair EMA grid on each new symbol with `scripts/run_grid.py --resume results/20261019_135940_grid`).
6. **If none exist:** record pass in log, set state to `AWAITING_NEW_ELIGIBLE_CANDIDATES`, next bound +24h.
7. **Update handoffs:** update `NEXT_AGENT_TASK.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with new bound and next unprocessed batch (or "none").

## Constraints
- No provider call before 2026-10-24T12:28:28.949476Z
- No second writer on `results/20261019_135940_grid`; no promotion from partial child grid
- No change to registered costs, folds, entry/exit semantics, or §3.4 gates
- Do not combine variables (`--min-risk-atr`, `--rr`, `--aggressive-exit`)
- Do not stop program because of failures - expand descending market cap per PROMPT.md §2.1.4, §6.7
