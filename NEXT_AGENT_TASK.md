# NEXT AGENT TASK

## Current state (verified against the saved artifacts, 2026-10-20T13:10:00Z)

**Program status: `EXPANSION_AVAILABLE`.** Batch 18 (universe N 177 -> 187) is **complete**: the 66-pair EMA grid is finished for all 187 symbols, the aggregate and the OOS + 2x-cost candidate check have been re-run, and the expansion log records the outcome. The universe is **not** exhausted: the current ranking snapshot still holds 79 eligible unseen names below the floor, so the next batch can be applied from the saved snapshot **without** querying CoinGecko again.

- Universe: **N = 187**, last symbol SSV/USDT at **USD 37 149 593** (the floor). `universe/mcap_rank.json`, snapshot `mcap_snapshot_20261020_113004` (CoinGecko, fetched 2026-10-20T11:30:04Z, pages 1-10, 1 000 ranked entries down to $15 174 185 - the pass reaches below the floor).
- Grid: **12 342 / 12 342 cells complete** in `results/20261019_135940_grid/` (187 symbols x 66 EMA pairs); 0 blocked.
- Decision count: **12 317 rejected**, 25 exploratory at the aggregate scan, and **0 credible candidates** after the OOS + 2x-cost check.
- Pooled, full-sample net of costs (10 bps taker + 2 bps slippage per side): mean net profit factor **0.4934**, median **0.5134**, best in-sample PF **2.2274** (BABYDOGE/USDT P50_55; rejected, zero OOS trades), **10 110 532 trades**.
- Cells with full-sample net PF > 1: **35 / 12 342 (0.28%)**. All 35 failed the required OOS and 2x-cost checks. The OOS window is the trailing 35% of each symbol's bars. No credible cell has been found.
- Candidate-check artifact: `results/20261020_125819_candidate_check/summary.md`. Requirements for credibility remain: OOS net PF > 1, OOS Sharpe > 0, at least 30 OOS trades, and PF > 1 under 2x fees/slippage.
- Tests last recorded: `python -m pytest tests/ -q` -> **56 passed** (verified 2026-10-20T12:52:00Z). No code changes in this session.

**Machine-readable state:** `universe/last_scan.json` - `state=EXPANSION_AVAILABLE`, `universe_n=187`, floor `SSV/USDT 37 149 593`, `eligible_unseen_below_floor_count=79`, `batch_selected` = the 10 batch-19 names below, `next_eligible_refresh_at=null` (no waiting is required because the snapshot still holds eligible names).

**Do not wait 24 hours.** The 24h refresh bound in PROMPT.md §2.1.5 applies only when a ranking pass yields **zero** eligible unseen names. The 2026-10-20T11:30:04Z pass was not empty, so the next batch is applied from that saved snapshot. A fresh CoinGecko pull would only be allowed from 2026-10-21T11:30:04Z, and is not needed for batch 19.

## Required next action - apply and process batch 19

1. **Reconcile state first.** Read this handoff, `PROMPT.md` §2.1, `universe/mcap_rank.json`, `universe/last_scan.json`, `universe/mcap_snapshot_20261020_113004.json`, `universe/mcap_expansion_log.md`, the grid `progress.json` and the latest candidate-check artifact. Do not repeat a completed scan and do not re-run finished grid cells.
2. **Apply the next 10 names from the saved snapshot** (verified by dry run at 2026-10-20T13:07Z; they are the 10 highest-ranked eligible names strictly below the floor, in descending market-cap order):

   | Rank in snapshot | Symbol | Market cap (USD) | Fixture on disk? |
   |---|---|---|---|
   | 572 | OSMO/USDT | 37 083 307 | no |
   | 574 | MOODENG/USDT | 37 050 928 | yes (`data/fixtures/MOODENG_USDT.csv`, 18 073 rows) |
   | 580 | MEW/USDT | 36 350 256 | no |
   | 590 | MERL/USDT | 35 731 205 | no |
   | 598 | RPL/USDT | 34 904 326 | no |
   | 599 | MOCA/USDT | 34 900 812 | no |
   | 601 | UMA/USDT | 34 706 377 | no |
   | 615 | DEGEN/USDT | 33 756 064 | no |
   | 619 | ORBS/USDT | 33 552 511 | no |
   | 623 | CATI/USDT | 33 051 490 | no |

   `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --apply-from universe/mcap_snapshot_20261020_113004.json --batch-size 10 --apply`

   Apply only from the reviewed saved snapshot. Preserve append-only global ordering: never remove or reorder existing rows. The apply step rewrites `universe/last_scan.json`; that is expected.
3. **Fetch and validate the new hourly OHLCV fixtures** for the 9 symbols that have none:
   `PYTHONPATH=. python3 scripts/fetch_kucoin.py --target-bars 22000 --symbols OSMO/USDT MEW/USDT MERL/USDT RPL/USDT MOCA/USDT UMA/USDT DEGEN/USDT ORBS/USDT CATI/USDT`
   then reconcile provenance with `PYTHONPATH=. python3 scripts/fetch_kucoin.py --reconcile-manifest`.
   A transient API error is not proof of ineligibility: re-query a failed symbol as the existing prompt specifies before excluding it. Record coverage, gaps, duplicates, price/ticker identity and all exclusion reasons (the batch-18 validation recipe: no duplicate timestamps, contiguous 1h grid, no invalid OHLC rows, and `|log(last close / CoinGecko price)|` well inside the script's 0.20 tolerance).
4. **Run the entire 66-pair grid for each newly appended symbol** in strict market-cap order, checkpointing one symbol at a time. Resume the existing run; do not overwrite completed cells:
   `PYTHONPATH=. python3 scripts/run_grid.py --n <rank-in-working-universe> --resume results/20261019_135940_grid --note "universe expansion batch 19: N 187 -> 197 (<SYMBOL>/USDT, 66-pair EMA grid)"`
   Ranks 188-197 = OSMO, MOODENG, MEW, MERL, RPL, MOCA, UMA, DEGEN, ORBS, CATI. After each symbol, checkpoint its result (remote push, see "Environment"), then run `scripts/aggregate_grid.py --run results/20261019_135940_grid` and `scripts/candidate_check.py --run results/20261019_135940_grid`; update the expansion log, progress summary and this handoff with the actual outcome.
5. **When the saved snapshot's band is exhausted**, take a fresh descending market-cap snapshot with the existing script (`PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 10 --batch-size 10` as a dry run), inspect the timestamped snapshot it writes and the exact candidate/exclusion results, and extend the page count only if the pass does not reach below the current floor. Respect bounded retries and provider rate limits. If a complete pass yields zero eligible names, persist a truthful `AWAITING_NEW_ELIGIBLE_CANDIDATES` state with evidence and a next refresh time >= 24h out. Do not invent names, repeatedly hit providers, change the strategy baseline, or call a candidate credible on in-sample metrics.

## Known gaps and open items (carry these forward truthfully)

- **GAS (rank 320, $80.3M) and CCD (rank 533, $41.79M)** are eligible in the current snapshot but rank **above** the floor, so the strict "append only names strictly below the floor" rule (PROMPT.md §2.1.2) keeps them out of the universe. CCD's hourly fixture is already on disk (`data/fixtures/CCD_USDT.csv`); it enters the universe automatically if a later snapshot puts it below the floor. Do not insert either name out of market-cap order.
- **`data/fixtures/fetch_manifest.json` holds 189 rows**, not 187: the extra rows are the pre-fetched CCD and MOODENG files, which are not (yet) universe members. Reconcile rather than hand-edit.
- **One interrupted grid invocation is recorded** in `results/20261019_135940_grid/run_config.json` history (note "universe expansion batch 18 ... (SSV/USDT ...)"). It was a duplicate runner that was stopped after it had recomputed some PEOPLE cells concurrently with the real run. All 660 batch-18 cells were re-verified afterwards: every cell has complete artifacts, readable gzip blobs, trade-row counts matching `trade_count`, and reconciling equity curves; a re-computation of two cells reproduced identical metrics (differences were CSV text round-trip rounding only). No result was affected.
- **ETN history is shorter** than the rest of the batch (18 410 hourly bars from 2024-09-13, Electroneum's KuCoin listing). It still clears the registered 2-year minimum history filter, but its grid cells have fewer trades than the other batch-18 symbols.

## Guardrails

- Keep the universe append-only and strictly market-cap descending; add only new eligible symbols below the existing floor.
- Never stop merely because the grid or a batch produced no edge. A negative result on the registered rules is not authorization to close the program.
- Never lower data-history or liquidity requirements to force expansion. Distinguish a genuinely absent pair/history from a transient API error or an incomplete ranking scan.
- Never promote an in-sample winner without passing the preregistered OOS and doubled-cost gates. Preserve every prior result, candidate rejection and provenance record.
- Keep the registered baseline and 66-pair EMA grid unchanged unless a separately preregistered mutation is authorized.
- Run `python -m pytest tests/ -q` after code changes and report the exact results.

## Environment

Use `PYTHONPATH=. python3 scripts/...` from the repository root. Available data fixtures and all prior result artifacts are reusable; fetch only data for genuinely new symbols. Checkpoint durably after each finished symbol with `python scripts/remote_checkpoint.py --message "chore: grid <SYMBOL>"` (the workflow controller only allows a 30s push, so keep each delta small).

## Session update (2026-10-20T13:10:00Z)

- Reconciled the state left by the previous session: the batch-18 expansion to N=187 had been applied and the grid was interrupted at ETN (52/66 cells, not checkpointed in `progress.json`).
- Reconciled the fetch manifest: IOTX and SSV had fixtures on disk but no provenance row -> `--reconcile-manifest` added them (189 rows).
- Completed the batch-18 grid: ETN (66/66), PEOPLE, IOTX, SSV -> **12 342 / 12 342 cells**, 0 blocked.
- Verified all 660 batch-18 cells (artifacts present, gzip readable, trades/equity consistent, metrics reproducible). No code changes.
- Re-ran `scripts/aggregate_grid.py` and `scripts/candidate_check.py`: mean net PF 0.4934, 35 cells with net PF > 1, all rejected by OOS + 2x cost stress -> **0 credible candidates** (`results/20261020_125819_candidate_check/`).
- Updated `universe/mcap_expansion_log.md` with the batch-18 section, the cumulative state at N=187 and the batch-19 candidate list.
- Dry-ran the batch-19 selection from the saved snapshot: OSMO, MOODENG, MEW, MERL, RPL, MOCA, UMA, DEGEN, ORBS, CATI. `universe/last_scan.json` now records `EXPANSION_AVAILABLE` with 79 eligible unseen names below the floor.
- Tests: `python -m pytest tests/ -q` -> **56 passed**.
