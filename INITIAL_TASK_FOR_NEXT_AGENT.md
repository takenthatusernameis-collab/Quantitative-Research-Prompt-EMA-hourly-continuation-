# NEXT TASK — refresh bound 2026-10-24T12:28:28.949476Z

## Initial task message for the next agent

The program is in `AWAITING_NEW_ELIGIBLE_CANDIDATES` after batch 28 (the
2026-10-23T12:28:28Z pass found 0 eligible unseen names below the floor; the
2,000-entry CoinGecko ranking band is exhausted down to $3,441,774). The 24 h
refresh bound expires at 2026-10-24T12:28:28.949476Z. Do **not** contact
CoinGecko/KuCoin before that timestamp.

At/after the bound, run exactly one 20-page market-cap ranking pass, freeze the
snapshot for 24 h, re-check the band below the then-current floor, and either
expand the universe (append descending market-cap candidates, fetch OHLCV, run
the full 66-pair EMA grid on each new symbol into `results/20261019_135940_grid`)
or record the empty pass and re-arm the bound. Then update both handoff files.

## Latest offline check (2026-10-23T22:27 UTC, this session)

`eligible: False`, bound `2026-10-24T12:28:28.949476+00:00`, now
`2026-10-23T22:27:37+00:00`. Reason: bound not elapsed (~14 h 0 min remaining).
No provider contact made. State unchanged: `AWAITING_NEW_ELIGIBLE_CANDIDATES`,
`universe_n=275`, `eligible_unseen_below_floor_count=0`, `batch_selected=[]`.
Baseline grid `results/20261019_135940_grid` verified complete
(275 symbols x 66 pairs = 18150/18150 cells, `all_symbols_processed=true`,
`next_cell=null`, 0 blocked). A wakeup is scheduled for
`2026-10-24T12:29:00Z` (wku_16ae2dc2f001dy4r5HL8OY1Xwq) to resume after the bound.

## Steps

1. **Verify eligibility offline first:**
   ```bash
   PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"
   ```
   Must return `eligible: True`. If `False`, stop and report the bound; nothing is actionable yet (do not override the gate).

2. **Run exactly one 20-page market-cap ranking pass** (the only provider contact this cycle):
   ```bash
   PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20
   ```
   (`scripts/refresh_universe.py fetch` is the gated equivalent.) The tool freezes the snapshot for 24 h and writes the new bound into `universe/last_scan.json`.

3. **Re-check the band below the current floor** (`eligible_unseen_below_floor_count`).

4. **If candidates exist:** expand per PROMPT.md §2.1 — append the next lower market-cap candidates descending (track previous N → new N, rank range, log to `universe/mcap_expansion_log.md` with source/date), fetch OHLCV for each via `scripts/fetch_kucoin.py`, then run the full 66-pair EMA grid on each new symbol with `scripts/run_grid.py --resume results/20261019_135940_grid`. Never create a second writer on the baseline grid; never promote from a partial child grid.

5. **If no candidates exist:** record the pass (snapshot_id, fetch time, pages, floor, exclusions) in `universe/mcap_expansion_log.md`, set `universe/last_scan.json` back to `state = AWAITING_NEW_ELIGIBLE_CANDIDATES`, and let the next bound become +24 h from the new scan time.

6. **Update handoffs:** after completing (or determining no-candidates), update both `NEXT_AGENT_TASK.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with the new bound and the next unprocessed symbol/pair batch (or "none").

## Constraints

- No provider call before 2026-10-24T12:28:28.949476Z; no gate override without a written reason.
- No second writer on `results/20261019_135940_grid`; no promotion from a partial child grid.
- No change to registered costs, folds, entry/exit semantics, or §3.4 gates.
- Do not combine variables (`--min-risk-atr`, `--rr`, `--aggressive-exit`).
- Do not stop on failures — expand descending market cap and continue per PROMPT.md §2.1.4, §6.7.
- Tests: `pytest`/`numpy`/`pandas` are installed (pytest 9.1.1, numpy 2.5.4, pandas 3.1.0). If reset, install first (`pip3 install pytest numpy pandas`) before `PYTHONPATH=. python3 -m pytest tests/ -q`. Expect 248/249 to pass; the one failure (`test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible`) is a pre-existing clock-relative-test bug — do not loosen the gate to fix it.

(End of file - total 62 lines)