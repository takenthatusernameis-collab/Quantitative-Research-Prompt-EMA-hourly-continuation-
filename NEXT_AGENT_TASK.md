# NEXT TASK — refresh bound 2026-10-24T12:28:28.949476Z

## Update 2026-10-23T20:39 UTC (current session)

Offline eligibility re-check (no provider contact): `eligible: False`, bound
`2026-10-24T12:28:28.949476+00:00`, now `2026-10-23T20:39:59+00:00`.
Reason: "the 24 h refresh bound 2026-10-24T12:28:28.949476+00:00 has not elapsed
yet". ~16 h remaining. Nothing actionable until the bound.

State confirmed unchanged from batch 28:
- `universe/last_scan.json`: `state=AWAITING_NEW_ELIGIBLE_CANDIDATES`, `universe_n=275`,
  `snapshot_id=mcap_snapshot_20261023_122828`, `scanned_at=2026-10-23T12:28:28.949476+00:00`,
  `eligible_unseen_below_floor_count=0`, `batch_selected=[]`,
  `next_eligible_refresh_at=2026-10-24T12:28:28.949476+00:00`.
- Baseline grid `results/20261019_135940_grid`: `completed_cells=18150` (275 symbols x 66
  pairs), `n_symbols=275`, `n_pairs=66`, `all_symbols_processed=true`, `next_cell=null`,
  no second writer. `summary.json` pooled: mean net PF 0.4987, median 0.5198,
  37 cells net PF > 1 (0.20%), 27 exploratory, 18123 rejected, 0 blocked, 0 credible
  candidates. `mutations.json`: `C_stricter_trend` and `C_min_risk_atr` both NOT_PROMOTED.

Environment note for the next agent: `pytest`, `numpy` and `pandas` are installed in
this sandbox (pytest 9.1.1, numpy 2.5.4, pandas 3.1.0). If the sandbox is reset,
install them before running `PYTHONPATH=. python3 -m pytest tests/ -q`.
One pre-existing test is failing for a reason unrelated to any code change:
`tests/test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible`
hard-codes `assert gate.gate_status(record)['eligible'] is False` against a fixed
bound of `2026-10-23T12:00:00+00:00`, so it fails whenever `now` is past that bound
(it is: 20:39 UTC). 248/249 tests pass. Do not "fix" it by loosening the gate; the
correct fix is to make the test clock-relative, and only if the next agent touches
that file.

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
- Tests: `pytest`/`numpy`/`pandas` are not preinstalled in the sandbox; install them
  first (`pip3 install pytest numpy pandas`) before running
  `PYTHONPATH=. python3 -m pytest tests/ -q`. Expect 248/249 to pass; the one
  failure (`test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible`)
  is a pre-existing clock-relative-test bug — do not loosen the gate to fix it.
## Update 2026-10-23T20:40 UTC (current session)

Offline eligibility re-check (no provider contact): `eligible: False`, bound
`2026-10-24T12:28:28.949476+00:00`, now `2026-10-23T20:40:56+00:00`.
Reason: "the 24 h refresh bound 2026-10-24T12:28:28.949476+00:00 has not elapsed
yet". ~16 h remaining. Nothing actionable until the bound; no provider contact made.

## Update 2026-10-23T21:06 UTC (current session)

Offline eligibility re-check (no provider contact): `eligible: False`, bound
`2026-10-24T12:28:28.949476+00:00`, now `2026-10-23T21:06:17+00:00`.
Reason: "the 24 h refresh bound 2026-10-24T12:28:28.949476+00:00 has not
elapsed yet". ~15 h remaining. Nothing actionable until the bound; no provider
contact made. State unchanged from batch 28 (see above).
