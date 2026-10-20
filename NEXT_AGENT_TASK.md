# NEXT AGENT TASK

## Current state (verified against the saved artifacts, 2026-10-20T15:35:00Z)

**Program status: `EXPANSION_AVAILABLE`.** Batch 20 (universe N 197 -> 207) is **complete**: the 66-pair EMA grid is finished for all 207 symbols, the aggregate and the OOS + 2x-cost candidate check have been re-run, and the expansion log records the outcome. The universe is **not** exhausted: the current ranking snapshot still holds 59 eligible unseen names below the floor, so the next batch can be applied from the saved snapshot **without** querying CoinGecko again.

- Universe: **N = 207**, last symbol XCH/USDT at **USD 29 168 720** (the floor). `universe/mcap_rank.json`, snapshot `mcap_snapshot_20261020_113004` (CoinGecko, fetched 2026-10-20T11:30:04Z, pages 1-10, 1 000 ranked entries down to $15 174 185 - the pass reaches below the floor).
- Grid: **13 662 / 13 662 cells complete** in `results/20261019_135940_grid/` (207 symbols x 66 EMA pairs); 0 blocked. `progress.json` reports `next_cell: null`.
- Decision count: **13 636 rejected**, 26 exploratory at the aggregate scan, and **0 credible candidates** after the OOS + 2x-cost check.
- Pooled, full-sample net of costs (10 bps taker + 2 bps slippage per side): mean net profit factor **0.4980**, median **0.5188**, best in-sample PF **2.2274** (BABYDOGE/USDT P50_55; rejected, zero OOS trades), **11 161 425 trades**.
- Cells with full-sample net PF > 1: **36 / 13 662 (0.26 %)**. All 36 failed the required OOS and 2x-cost checks. The OOS window is the trailing 35% of each symbol's bars. No credible cell has been found.
- Candidate-check artifact: `results/20261020_152413_candidate_check/summary.md` (36 cells, 36 rejected). Requirements for credibility remain: OOS net PF > 1, OOS Sharpe > 0, at least 30 OOS trades, and PF > 1 under 2x fees/slippage.
- Tests last recorded: `python -m pytest tests/ -q` -> **56 passed** (verified 2026-10-20T15:33:00Z). No code changes in this session.

**Machine-readable state:** `universe/last_scan.json` - `state=EXPANSION_AVAILABLE`, `universe_n=207`, floor `XCH/USDT 29 168 720`, `eligible_unseen_below_floor_count=59`, `batch_selected` = the 10 batch-21 names below, `next_eligible_refresh_at=null` (no waiting is required because the snapshot still holds eligible names).

**Do not wait 24 hours.** The 24h refresh bound in PROMPT.md §2.1.5 applies only when a ranking pass yields **zero** eligible unseen names. The 2026-10-20T11:30:04Z pass was not empty, so the next batch is applied from that saved snapshot. A fresh CoinGecko pull would only be allowed from 2026-10-21T11:30:04Z, and is not needed for batch 21.

## Required next action - apply and process batch 21

1. **Reconcile state first.** Read this handoff, `PROMPT.md` §2.1, `universe/mcap_rank.json`, `universe/last_scan.json`, `universe/mcap_snapshot_20261020_113004.json`, `universe/mcap_expansion_log.md`, the grid `progress.json` and the latest candidate-check artifact. Do not repeat a completed scan and do not re-run finished grid cells.
2. **Apply the next 10 names from the saved snapshot** (verified by dry run at 2026-10-20T15:25Z; they are the 10 highest-ranked eligible names strictly below the floor, in descending market-cap order):

   | Rank in snapshot | Symbol | Name | Market cap (USD) | Fixture on disk? |
   |---|---|---|---|---|
   | 687 | ELON/USDT | Dogelon Mars | 28 983 090 | no |
   | 689 | CTSI/USDT | Cartesi | 28 823 155 | no |
   | 693 | IOST/USDT | IOST | 28 658 475 | no |
   | 699 | SWFTC/USDT | SWFTCOIN | 28 193 368 | no |
   | 705 | UQC/USDT | Uquid Coin | 27 726 441 | no |
   | 709 | ILV/USDT | Illuvium | 27 459 683 | no |
   | 712 | AVA/USDT | AVA (Travala) | 27 100 879 | no |
   | 716 | CPOOL/USDT | Clearpool | 26 920 775 | no |
   | 717 | BLUR/USDT | Blur | 26 892 547 | no |
   | 720 | EUL/USDT | Euler | 26 770 327 | no |

   `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --apply-from universe/mcap_snapshot_20261020_113004.json --batch-size 10 --apply`

   Apply only from the reviewed saved snapshot. Preserve append-only global ordering: never remove or reorder existing rows. The apply step rewrites `universe/last_scan.json`; that is expected. Re-run the same command **without** `--apply` afterwards to refresh `last_scan.json` against the new N (the previous agent left it one batch stale after applying).
3. **Fetch and validate the new hourly OHLCV fixtures** for the 10 symbols that have none:
   `PYTHONPATH=. python3 scripts/fetch_kucoin.py --target-bars 22000 --symbols ELON/USDT CTSI/USDT IOST/USDT SWFTC/USDT UQC/USDT ILV/USDT AVA/USDT CPOOL/USDT BLUR/USDT EUL/USDT`
   then reconcile provenance with `PYTHONPATH=. python3 scripts/fetch_kucoin.py --reconcile-manifest`.
   A transient API error is not proof of ineligibility: re-query a failed symbol as the existing prompt specifies before excluding it. Record coverage, gaps, duplicates, price/ticker identity and all exclusion reasons (the batch-20 validation recipe: no duplicate timestamps, contiguous 1h grid with no missing hours, no invalid OHLC rows, and `|log(last close / CoinGecko price)|` well inside the script's 0.20 tolerance).
   **Price-scale warning:** ELON/USDT trades at ~2.9e-08 USD, so the fixed 12 bps per-side cost is a large fraction of every bar move. The same happened with AINFT (`NFT`) in batch 8: it is a valid test of the registered rules, but its result is dominated by cost drag rather than signal quality, and its cell trade counts explode. Expect and report this rather than treating it as a defect.
4. **Run the entire 66-pair grid for each newly appended symbol** in strict market-cap order, checkpointing one symbol at a time. Resume the existing run; do not overwrite completed cells:
   `PYTHONPATH=. python3 scripts/run_grid.py --n <rank-in-working-universe> --resume results/20261019_135940_grid --note "universe expansion batch 21: N 207 -> 217 (<SYMBOL>/USDT, 66-pair EMA grid)"`
   Ranks 208-217 = ELON, CTSI, IOST, SWFTC, UQC, ILV, AVA, CPOOL, BLUR, EUL. One `--n` invocation per symbol keeps the checkpoint delta small; the runner skips already-completed cells by itself. After each symbol, checkpoint its result (remote push, see "Environment"), then run `scripts/aggregate_grid.py --run results/20261019_135940_grid` and `scripts/candidate_check.py --run results/20261019_135940_grid`; update the expansion log, progress summary and this handoff with the actual outcome.
5. **When the saved snapshot's band is exhausted** (59 eligible names remain below the floor now, so this is not close), take a fresh descending market-cap snapshot with the existing script (`PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 10 --batch-size 10` as a dry run), inspect the timestamped snapshot it writes and the exact candidate/exclusion results, and extend the page count only if the pass does not reach below the current floor. Respect bounded retries and provider rate limits. If a complete pass yields zero eligible names, persist a truthful `AWAITING_NEW_ELIGIBLE_CANDIDATES` state with evidence and a next refresh time >= 24h out. Do not invent names, repeatedly hit providers, change the strategy baseline, or call a candidate credible on in-sample metrics.

## Known gaps and open items (carry these forward truthfully)

- **GAS (rank 320, $80.3M) and CCD (rank 533, $41.79M)** are eligible in the current snapshot but rank **above** the floor, so the strict "append only names strictly below the floor" rule (PROMPT.md §2.1.2) keeps them out of the universe. CCD's hourly fixture is already on disk (`data/fixtures/CCD_USDT.csv`); it enters the universe automatically if a later snapshot puts it below the floor. Do not insert either name out of market-cap order.
- **`data/fixtures/fetch_manifest.json` holds 208 rows**, not 207: the extra row is the pre-fetched CCD file, which is not a universe member. Reconcile rather than hand-edit.
- **The batch-19 section of `universe/mcap_expansion_log.md` was missing** and has been reconstructed in this session from the artifacts (grid `per_symbol.json`, the `results/20261020_141749_candidate_check/` candidate check and the fetch manifest). Its numbers are artifact-derived, not remembered; re-verify against those files if you touch them.
- **REZ/USDT (batch 20) is the strongest single symbol in the program** (mean net PF 0.6629 over 51 445 trades) and BABYDOGE/USDT (batch 14) is the only symbol whose mean net PF exceeds 1.0 (1.0628) - but on just 2 775 trades across 66 cells, with zero OOS trades in every one of its 32 above-PF cells. Both are multiple-testing noise, not edges.
- **Thin pairs quote-carry** (bars with zero volume but moving OHLC): LISTA 12.9 %, GTC 11.5 %, MAGIC 9.3 % of bars in batch 20. This is a known property of the data layer, not a defect; a zero-volume-bar filter would be a registered mutation (§5), not a silent change.

## Guardrails

- Keep the universe append-only and strictly market-cap descending; add only new eligible symbols below the existing floor.
- Never stop merely because the grid or a batch produced no edge. A negative result on the registered rules is not authorization to close the program.
- Never lower data-history or liquidity requirements to force expansion. Distinguish a genuinely absent pair/history from a transient API error or an incomplete ranking scan.
- Never promote an in-sample winner without passing the preregistered OOS and doubled-cost gates. Preserve every prior result, candidate rejection and provenance record.
- Keep the registered baseline and 66-pair EMA grid unchanged unless a separately preregistered mutation is authorized.
- Run `python -m pytest tests/ -q` after code changes and report the exact results.

## Environment

Use `PYTHONPATH=. python3 scripts/...` from the repository root. Available data fixtures and all prior result artifacts are reusable; fetch only data for genuinely new symbols. Checkpoint durably after each finished symbol with `python scripts/remote_checkpoint.py --message "chore: grid <SYMBOL>"` (the workflow controller only allows a 30s push, so keep each delta small).

## Session update (2026-10-20T15:35:00Z)

- Completed the interrupted batch-19 candidate check (`results/20261020_141749_candidate_check/`): 36/36 cells, all rejected, 0 credible candidates. The only new in-sample survivor was MOODENG/USDT P8_200 (net PF 1.0567), which fails out-of-sample (0.8576, Sharpe -0.9291 over 121 OOS trades) and cost stress (0.8999).
- Applied batch 20 from the saved snapshot `mcap_snapshot_20261020_113004.json`: universe **N 197 -> 207** (METIS, REZ, LISTA, COTI, MAGIC, GTC, MANTA, LUNA, FLUX, XCH). The dry run and the applied run agree exactly with the names named in the previous handoff.
- Fetched all 10 new hourly fixtures from the KuCoin public candles API (22 000 bars target, 1h, UTC) and validated them: no duplicate timestamps, no missing hours, no invalid OHLC rows, and every price-identity gap within 0.065 in log terms (script tolerance 0.20). Manifest reconciled to 208 rows.
- Ran the 66-pair grid for all 10 new symbols (ranks 198-207) and verified every cell: complete artifacts, matching trade counts, reconciling equity curves, and the registered baseline config (10 bps taker + 2 bps slippage, RR 1.0, risk sizing, conservative exit). **13 662 / 13 662 cells** complete, 0 blocked.
- Re-ran `scripts/aggregate_grid.py` and `scripts/candidate_check.py`: mean net PF 0.4980, median 0.5188, 36 cells with net PF > 1, all rejected by OOS + 2x cost stress -> **0 credible candidates** (`results/20261020_152413_candidate_check/`). Batch 20 added **no** cell above net PF 1.
- Updated `universe/mcap_expansion_log.md`: added the missing batch-19 section, the new batch-20 section, the cumulative state at N=207 and the batch-21 candidate list. Refreshed `universe/last_scan.json` against the N=207 universe.
- Tests: `python -m pytest tests/ -q` -> **56 passed**. No code changes in this session.
