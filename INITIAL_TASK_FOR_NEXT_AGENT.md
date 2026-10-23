# NEXT TASK — refresh bound 2026-10-24T12:28:28.949476Z

**Run at/after 2026-10-24T12:28:28.949476Z. Do NOT contact the provider (CoinGecko / KuCoin) before that timestamp.**

## Current state (verified this session, 2026-10-23T17:48 UTC)

| Item | Value |
|---|---|
| Refresh gate | `eligible: False` — bound 2026-10-24T12:28:28.949476+00:00 has not elapsed |
| Program state | `AWAITING_NEW_ELIGIBLE_CANDIDATES` |
| Universe | N = 275, floor `BOSON/USDT` $3 558 643 |
| Frozen snapshot | `universe/mcap_snapshot_20261023_122828.json` (20 pages / 2 000 entries, lowest mcap $3 441 774, coverage reaches below floor) |
| Baseline grid | `results/20261019_135940_grid` — **18 150/18 150 cells complete, 0 blocked**, `all_symbols_processed=true`, `next_cell=null` |
| Baseline outcome | pooled mean net PF 0.4987, median 0.5198, 37 cells net PF > 1 (0.20 % vs ~50 % null), 27 exploratory, 18 123 rejected, **0 credible candidates** |
| Mutations | `C_stricter_trend` and `C_min_risk_atr` both **NOT_PROMOTED** (recorded in `results/mutations.json`) |
| Null grid scan | `results/20261023_050716_null_grid_scan/` — no edge (6 real cells clear the §3.4 gate vs 24 block-null) |

## Your task (in order)

1. **Verify eligibility offline first** (no provider contact):
   `PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"` → must return `eligible: True`. If it returns `eligible: False`, stop and report the bound; nothing is actionable yet.
2. **Run exactly one 20-page market-cap ranking pass:**
   `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20`
   (or `scripts/refresh_universe.py fetch`). This is the only provider contact in this cycle.
3. **Freeze the new snapshot for 24 h** (the tool writes the bound into `universe/last_scan.json`).
4. **Re-check the band below the then-current floor** for eligible unseen candidates (`eligible_unseen_below_floor_count`).
5. **If candidates exist**, expand the universe per PROMPT.md §2.1: append next lower market-cap candidates in descending order (previous N → new N, rank range added, source/date in `universe/mcap_expansion_log.md`), fetch OHLCV for each new symbol via `scripts/fetch_kucoin.py`, then run the full 66-pair EMA grid on each new symbol with `scripts/run_grid.py --resume results/20261019_135940_grid`.
6. **If no candidates exist**, record the pass (snapshot id, fetch time, page coverage, floor, exclusions) and set state back to `AWAITING_NEW_ELIGIBLE_CANDIDATES`; the next refresh bound is then +24 h.
7. Log the pass in `universe/mcap_expansion_log.md`, then update `NEXT_AGENT_TASK.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with the next bound and the next unprocessed symbol/pair batch.

## What must not happen

- No provider call before 2026-10-24T12:28:28.949476Z.
- No second writer on `results/20261019_135940_grid`; no promotion from a partial child grid.
- No change to registered costs, folds, entry/exit semantics, or §3.4 gates.
- Do not combine variables (`--min-risk-atr`, `--rr`, `--aggressive-exit`) in any run.
- Do not stop the program because prior pairs/symbols failed — expand descending market cap and continue (PROMPT.md §2.1.4, §6.7).
