# NEXT TASK — refresh bound 2026-10-24T12:28:28.949476Z (updated 2026-10-24T00:42 UTC)

## Current status (current session)
- State: `AWAITING_NEW_ELIGIBLE_CANDIDATES`
- `universe/last_scan.json`: `universe_n=275`, `eligible_unseen_below_floor_count=0`, `batch_selected=[]`, `snapshot_id=mcap_snapshot_20261023_122828`, `scanned_at=2026-10-23T12:28:28.949476+00:00`
- Baseline grid `results/20261019_135940_grid`: complete (18150/18150 cells, 275 symbols × 66 pairs). Pooled summary mean net PF 0.4987, 37 cells net PF > 1, 0 credible candidates.
- Gate check (offline, confirmed 2026-10-24T00:42 UTC): `eligible: False`, bound `2026-10-24T12:28:28.949476+00:00`, now `2026-10-24T00:42:27.679899+00:00`. Reason: bound not elapsed (~11h 46m remaining). No provider contact made.
- Wakeup scheduled: `wku_16b564aff001EO27sZd4koqdLw` at 2026-10-24T12:29:00Z to resume automatically. If harness does not resume, run steps at/after bound.

## Your task (run at/after 2026-10-24T12:28:28.949476Z)
**Do NOT** contact provider (CoinGecko/KuCoin) before that timestamp.

1. **Verify eligibility offline first:**
   ```bash
   PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"
   ```
   Must return `eligible: True`. If `False`, stop and report bound; nothing actionable yet.

2. **Run exactly one 20-page market-cap ranking pass:**
   ```bash
   PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20
   ```
   (or `scripts/refresh_universe.py fetch`). This is the only provider contact this cycle. The tool freezes snapshot for 24h and writes new bound to `universe/last_scan.json`.

3. **Re-check band below current floor** for eligible unseen candidates (`eligible_unseen_below_floor_count`).

4. **If candidates exist:** Expand per PROMPT.md §2.1 - append next lower market-cap candidates descending (track previous→new N, rank range, log to `universe/mcap_expansion_log.md` with source/date). Fetch OHLCV for each via `scripts/fetch_kucoin.py`. Run full 66-pair EMA grid on each new symbol with `scripts/run_grid.py --resume results/20261019_135940_grid`. Never create second writer on baseline grid; never promote from partial child grid.

5. **If no candidates exist:** Record pass (snapshot_id, fetch time, pages, floor, exclusions) in `universe/mcap_expansion_log.md`. Set state back to `AWAITING_NEW_ELIGIBLE_CANDIDATES` in `universe/last_scan.json`; next bound becomes +24h from new scan time.

6. **Update handoffs:** After completing (or determining no-candidates), update both `NEXT_AGENT_TASK.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with the new bound and next unprocessed symbol/pair batch (or "none").

## Constraints
- No provider call before 2026-10-24T12:28:28.949476Z
- No second writer on `results/20261019_135940_grid`; no promotion from partial child grid
- No change to registered costs, folds, entry/exit semantics, or §3.4 gates
- Do not combine variables (`--min-risk-atr`, `--rr`, `--aggressive-exit`)
- Do not stop program due to failures - expand descending market cap and continue per PROMPT.md §2.1.4, §6.7
- Tests: `pytest` 9.1.1, `numpy` 2.5.4, `pandas` 3.1.0 installed. Expect 248/249 pass; `test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible` is pre-existing clock-relative bug — do not loosen gate.
