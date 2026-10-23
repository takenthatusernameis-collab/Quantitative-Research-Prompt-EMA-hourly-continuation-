# NEXT TASK — refresh bound 2026-10-24T12:28:28.949476Z

## Update 2026-10-23T19:44 UTC (current session)

Offline verification completed (no provider contact).
- `PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"` → `{'eligible': False, 'bound': '2026-10-24T12:28:28.949476+00:00', 'now': '2026-10-23T19:44:50+00:00', 'reason': 'the 24 h refresh bound 2026-10-24T12:28:28.949476+00:00 has not elapsed yet'}`
- `universe/last_scan.json`: `state=AWAITING_NEW_ELIGIBLE_CANDIDATES`, `universe_n=275`, `snapshot_id=mcap_snapshot_20261023_122828`, `scanned_at=2026-10-23T12:28:28.949476+00:00`, 20 pages/2000 entries, lowest $3,441,774, `expansion_floor=BOSON/USDT $3,558,643`, `eligible_unseen_below_floor_count=0`, `batch_selected=[]`, `next_eligible_refresh_at=2026-10-24T12:28:28.949476+00:00`
- Baseline grid `results/20261019_135940_grid`: 18150/18150 cells complete, 0 blocked, 0 incomplete, 0 missing fixtures. 0 credible candidates.
- `results/mutations.json`: `C_stricter_trend` and `C_min_risk_atr` both **NOT_PROMOTED**.
- Null grid `results/20261023_050716_null_grid_scan/`: no edge.

**Status:** Nothing actionable before bound. Waiting for next refresh window.

## Your task (run at/after 2026-10-24T12:28:28.949476Z)

Do **NOT** contact provider (CoinGecko/KuCoin) before that timestamp.

1. **Verify eligibility offline first:**
   ```bash
   PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"
   ```
   Must return `eligible: True`. If `False`, stop and report bound; nothing actionable yet.

2. **Run exactly one 20-page market-cap ranking pass:**
   ```bash
   PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20
   ```
   (or `scripts/refresh_universe.py fetch`). This is the only provider contact this cycle.

3. **Freeze snapshot for 24h** (tool writes bound to `universe/last_scan.json`).

4. **Re-check band below current floor** for eligible unseen candidates (`eligible_unseen_below_floor_count`).

5. **If candidates exist:** Expand per PROMPT.md §2.1 - append next lower market-cap candidates descending (track previous→new N, rank range, log to `universe/mcap_expansion_log.md` with source/date). Fetch OHLCV for each via `scripts/fetch_kucoin.py`. Run full 66-pair EMA grid on each new symbol with `scripts/run_grid.py --resume results/20261019_135940_grid`. Never create second writer on baseline grid; never promote from partial child grid.

6. **If no candidates exist:** Record pass (snapshot_id, fetch time, pages, floor, exclusions) in `universe/mcap_expansion_log.md`. Set state back to `AWAITING_NEW_ELIGIBLE_CANDIDATES` in `universe/last_scan.json`; next bound becomes +24h from new scan time.

7. **Update handoffs:** After completing (or determining no-candidates), update both `NEXT_AGENT_TASK.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with the new bound and next unprocessed symbol/pair batch (or "none").

## Constraints
- No provider call before 2026-10-24T12:28:28.949476Z
- No second writer on `results/20261019_135940_grid`; no promotion from partial child grid
- No change to registered costs, folds, entry/exit semantics, or §3.4 gates
- Do not combine variables (`--min-risk-atr`, `--rr`, `--aggressive-exit`)
- Do not stop program due to failures - expand descending market cap and continue per PROMPT.md §2.1.4, §6.7