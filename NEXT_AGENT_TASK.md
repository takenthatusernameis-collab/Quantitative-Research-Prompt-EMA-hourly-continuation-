# NEXT AGENT TASK

## Current state (verified against the saved artifacts, 2026-10-20T20:12:00Z)

**Program status: `EXPANSION_AVAILABLE`.** Batch 23 (universe N 227 -> 237) is **complete**: the 66-pair EMA grid is finished for all 237 symbols, the aggregate and the OOS + 2x-cost candidate check have been re-run, and the expansion log records the outcome. The universe is **not** exhausted: the current ranking snapshot still holds 29 eligible unseen names below the floor, so the next batch can be applied from the saved snapshot **without** querying CoinGecko again.

- Universe: **N = 237**, last symbol GMT/USDT at **USD 22 410 555** (the floor). `universe/mcap_rank.json`, snapshot `mcap_snapshot_20261020_113004` (CoinGecko, fetched 2026-10-20T11:30:04Z, pages 1-10, 1 000 ranked entries down to $15 174 185 - the pass reaches below the floor).
- Grid: **15 642 / 15 642 cells complete** in `results/20261019_135940_grid/` (237 symbols x 66 EMA pairs); 0 blocked. `progress.json` reports `next_cell: null` and `all_symbols_processed: true`.
- Decision count: **15 616 rejected**, 26 exploratory at the aggregate scan, and **0 credible candidates** after the OOS + 2x-cost check.
- Pooled, full-sample net of costs (10 bps taker + 2 bps slippage per side): mean net profit factor **0.4943**, median **0.5141**, best in-sample PF **2.2274** (BABYDOGE/USDT P50_55; rejected, zero OOS trades), **12 705 984 trades**.
- Cells with full-sample net PF > 1: **36 / 15 642 (0.23 %)**. All 36 failed the required OOS and 2x-cost checks, and the set is **unchanged from batch 20** (32 BABYDOGE cells with zero OOS trades, JASMY P20_200, JASMY P21_200, SUPER P8_200, MOODENG P8_200). The OOS window is the trailing 35% of each symbol's bars. Batch 23 added no survivor.
- Candidate-check artifact: `results/20261020_200452_candidate_check/summary.md` (36 cells, 36 rejected). Requirements for credibility remain: OOS net PF > 1, OOS Sharpe > 0, at least 30 OOS trades, and PF > 1 under 2x fees/slippage.
- Tests last recorded: `python -m pytest tests/ -q` -> **56 passed** (re-verified 2026-10-20T20:10:00Z). No code changes in this session.

**Machine-readable state:** `universe/last_scan.json` - `state=EXPANSION_AVAILABLE`, `universe_n=237`, floor `GMT/USDT 22 410 555`, `eligible_unseen_below_floor_count=29`, `batch_selected` = the 10 batch-24 names below, `next_eligible_refresh_at=null` (no waiting is required because the snapshot still holds eligible names).

**Do not wait 24 hours.** The 24h refresh bound in PROMPT.md §2.1.5 applies only when a ranking pass yields **zero** eligible unseen names. The 2026-10-20T11:30:04Z pass was not empty, so the next batch is applied from that saved snapshot. A fresh CoinGecko pull would only be allowed from 2026-10-21T11:30:04Z, and is not needed for batch 24.

## Required next action - apply and process batch 24

1. **Reconcile state first.** Read this handoff, `PROMPT.md` §2.1, `universe/mcap_rank.json`, `universe/last_scan.json`, `universe/mcap_snapshot_20261020_113004.json`, `universe/mcap_expansion_log.md`, the grid `progress.json` and the latest candidate-check artifact. Do not repeat a completed scan and do not re-run finished grid cells.
2. **Apply the next 10 names from the saved snapshot** (they are the 10 highest-ranked eligible names strictly below the floor, in descending market-cap order):

   | Rank in snapshot | Universe rank | Symbol | Name | Market cap (USD) | Ranked CoinGecko price | Fixture on disk? |
   |---|---|---|---|---|---|---|
   | 816 | 238 | SATS/USDT | SATS (Ordinals) | 21 621 654 | 1.0297e-08 | no |
   | 818 | 239 | OGN/USDT | Origin Token | 21 533 963 | 0.02886994 | no |
   | 820 | 240 | CETUS/USDT | Cetus Protocol | 21 414 698 | 0.02218505 | no |
   | 824 | 241 | YGG/USDT | Yield Guild Games | 21 324 785 | 0.02369684 | no |
   | 835 | 242 | DODO/USDT | DODO | 20 845 043 | 0.02084181 | no |
   | 838 | 243 | ONE/USDT | Harmony | 20 634 662 | 0.00138669 | no |
   | 843 | 244 | AEVO/USDT | Aevo | 20 512 457 | 0.02199021 | no |
   | 844 | 245 | SLP/USDT | Smooth Love Potion | 20 466 559 | 0.00056532 | no |
   | 854 | 246 | CGPT/USDT | ChainGPT | 20 047 403 | 0.0214897 | no |
   | 862 | 247 | WOO/USDT | WOO | 19 716 095 | 0.01043945 | no |

   `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --apply-from universe/mcap_snapshot_20261020_113004.json --batch-size 10 --apply`

   Apply only from the reviewed saved snapshot. Preserve append-only global ordering: never remove or reorder existing rows. The apply step rewrites `universe/last_scan.json`; that is expected. Re-run the same command **without** `--apply` afterwards to refresh `last_scan.json` against the new N, and confirm the file then reports `universe_n=247`, floor `WOO/USDT`, `eligible_unseen_below_floor_count=19` and `batch_selected` = the ten names after WOO.
3. **Fetch and validate the new hourly OHLCV fixtures** for the 10 symbols that have none:
   `PYTHONPATH=. python3 scripts/fetch_kucoin.py --target-bars 22000 --symbols SATS/USDT OGN/USDT CETUS/USDT YGG/USDT DODO/USDT ONE/USDT AEVO/USDT SLP/USDT CGPT/USDT WOO/USDT`
   then reconcile provenance with `PYTHONPATH=. python3 scripts/fetch_kucoin.py --reconcile-manifest`.
   A transient API error is not proof of ineligibility: re-query a failed symbol as the existing prompt specifies before excluding it. Record coverage, gaps, duplicates, price/ticker identity and all exclusion reasons (the batch-20/batch-21/batch-22/batch-23 validation recipe: no duplicate timestamps, contiguous 1h grid with no missing hours, no invalid OHLC rows, and `|log(last close / CoinGecko price)|` well inside the script's 0.20 tolerance).
   **Ticker-collision check is mandatory for this batch.** The snapshot contains **two** `ONE` rows: rank 419 "ONEchain" ($54 939 516, price 0.101731) and rank 838 "Harmony" ($20 634 662, price 0.00138669). The ONEchain row is already excluded in the saved snapshot as `kucoin_pair_trades_a_different_asset` (the live KuCoin ONE-USDT price is Harmony's ~0.0014), so the eligible `ONE` in this batch **is Harmony**. Check the fetched ONE/USDT fixture's last close against the **Harmony** price, not the ONEchain price; if the fixture does not match Harmony within the 0.20 log tolerance, treat it as the `kucoin_pair_trades_a_different_asset` exclusion rather than as a data error. `DODO`, `CGPT`, `WOO`, `OGN`, `CETUS`, `YGG` and `AEVO` are also short tickers worth a live level-1 price check before the download.
   **Price-scale check:** **SATS is a sub-cent asset** (ranked price 1.0297e-08 USD), the same class as ELON (batch 21: 12 bps per side vs a 0.41 % median absolute hourly move, ~29x). Compute each new name's cost-to-move multiple (0.12 / median absolute hourly return) and report any name whose cost is a large multiple of its median absolute hourly move. Such a result measures cost drag rather than signal quality - report it, do not treat it as a defect. Batch 23 had no such name (multiples 0.19x-0.38x).
4. **Run the entire 66-pair grid for each newly appended symbol** in strict market-cap order, checkpointing one symbol at a time. Resume the existing run; do not overwrite completed cells:
   `PYTHONPATH=. python3 scripts/run_grid.py --n <rank-in-working-universe> --resume results/20261019_135940_grid --note "universe expansion batch 24: N 237 -> 247 (<SYMBOL>/USDT, 66-pair EMA grid)"`
   Ranks 238-247 = SATS, OGN, CETUS, YGG, DODO, ONE, AEVO, SLP, CGPT, WOO. Note the `--n` semantics: it is the **count** of symbols to process from the top of the market-cap ranking, so `--n 238` processes ranks 1-238 and the runner skips the 237 already-complete symbols, leaving exactly SATS's 66 cells; `--n 239` adds OGN, and so on. One `--n` invocation per symbol keeps the checkpoint delta small. After each symbol, checkpoint its result (remote push, see "Environment"), then run `scripts/aggregate_grid.py --run results/20261019_135940_grid` and `scripts/candidate_check.py --run results/20261019_135940_grid`; update the expansion log, progress summary and this handoff with the actual outcome.
5. **When the saved snapshot's band is exhausted** (29 eligible names remain below the floor now, so this is not close), take a fresh descending market-cap snapshot with the existing script (`PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 10 --batch-size 10` as a dry run), inspect the timestamped snapshot it writes and the exact candidate/exclusion results, and extend the page count only if the pass does not reach below the current floor. Respect bounded retries and provider rate limits. If a complete pass yields zero eligible names, persist a truthful `AWAITING_NEW_ELIGIBLE_CANDIDATES` state with evidence and a next refresh time >= 24h out. Do not invent names, repeatedly hit providers, change the strategy baseline, or call a candidate credible on in-sample metrics.

## Known gaps and open items (carry these forward truthfully)

- **GAS (rank 320, $80.3M) and CCD (rank 533, $41.79M)** are eligible in the current snapshot but rank **above** the floor, so the strict "append only names strictly below the floor" rule (PROMPT.md §2.1.2) keeps them out of the universe. CCD's hourly fixture is already on disk (`data/fixtures/CCD_USDT.csv`); it enters the universe automatically if a later snapshot puts it below the floor. Do not insert either name out of market-cap order.
- **The `ONE` ticker is ambiguous in the ranking** (ONEchain at rank 419, Harmony at rank 838). Only Harmony is eligible; keep it that way unless a fresh snapshot changes the exclusion.
- **`data/fixtures/fetch_manifest.json` holds 238 rows**, not 237: the extra row is the pre-fetched CCD file, which is not a universe member. Reconcile rather than hand-edit. (`data/fixtures/sample_hourly.csv` is a synthetic sample and is correctly absent from the manifest.)
- **PUFFER/USDT (17 671 bars from 2024-10-14) of batch 23 has the tightest history** in the program so far: only 151 bars above the 17 520-bar (2-year) eligibility floor. It still covers the largest `P_slow` (200) plus the trailing 35 % OOS window, but a name with a shorter history than that should be documented rather than dropped.
- **G/USDT (19 018 bars) and CARV/USDT (17 770 bars) of batch 22 have shorter histories** than the other eight (22 000 bars) because both listed later. Both still exceed the 17 520-bar (2-year) eligibility floor and cover the largest `P_slow` (200) plus the trailing 35 % OOS window.
- **UQC/USDT (batch 21) is an extremely thin pair**: 48.9 % of its bars have zero volume and 55.8 % close unchanged, so its trade count (377 per cell) and mean net PF (0.2053) are artefacts of a flat price, not a broken fixture. It has 0 zero-volume-but-moving-OHLC quote-carry bars. Do not "fix" it.
- **ELON/USDT (batch 21) is cost-dominated** (12 bps per side vs a 0.41 % median absolute hourly move). Its result measures cost drag, not signal quality. Batches 22 and 23 had no such name.
- **Thin pairs quote-carry** (bars with zero volume but moving OHLC): LISTA 12.9 %, GTC 11.5 %, MAGIC 9.3 % of bars in batch 20. This is a known property of the data layer, not a defect; a zero-volume-bar filter would be a registered mutation (§5), not a silent change. Batches 21, 22 and 23 had **no** quote-carry bars in any of their thirty fixtures.
- **REZ/USDT (batch 20) is the strongest single symbol in the program** (mean net PF 0.6629 over 51 445 trades) and BABYDOGE/USDT (batch 14) is the only symbol whose mean net PF exceeds 1.0 (1.0628) - but on just 2 775 trades across 66 cells, with zero OOS trades in every one of its 32 above-PF cells. Both are multiple-testing noise, not edges.
- **Batch 23's mean net PF (0.4932) is above batch 22's 0.4434 but still below the 0.5 no-edge mark**, and the per-batch means are flat-to-declining from b7 to b23 (b21 0.4697, b22 0.4434, b23 0.4932). The registered rule does not improve as market cap falls; this is the program-level finding, and it does not authorise stopping.
- The b7-b20 mean-net-PF-by-batch list printed in the batch-20 cumulative section of `universe/mcap_expansion_log.md` was misaligned by one entry from b14 onward; the batch-21/22/23 cumulative sections carry the recomputed lists (b7-b21, b7-b22, b7-b23) derived from `results/20261019_135940_grid/per_symbol.json` and the coverage table in the log. Use the recomputed one.
- The batch-23 candidate-check artifacts from this session (`results/20261020_190020_candidate_check`, `..._190750`, `..._191500`, `..._192144`, `..._192848`, `..._193603`, `..._194316`, `..._195031`, `..._195739`) are intermediate per-symbol snapshots; `results/20261020_200452_candidate_check` is the final one for the batch.

## Guardrails

- Keep the universe append-only and strictly market-cap descending; add only new eligible symbols below the existing floor.
- Never stop merely because the grid or a batch produced no edge. A negative result on the registered rules is not authorization to close the program.
- Never lower data-history or liquidity requirements to force expansion. Distinguish a genuinely absent pair/history from a transient API error or an incomplete ranking scan.
- Never promote an in-sample winner without passing the preregistered OOS and doubled-cost gates. Preserve every prior result, candidate rejection and provenance record.
- Keep the registered baseline and 66-pair EMA grid unchanged unless a separately preregistered mutation is authorized.
- Run `python -m pytest tests/ -q` after code changes and report the exact results.

## Environment

Use `PYTHONPATH=. python3 scripts/...` from the repository root. Available data fixtures and all prior result artifacts are reusable; fetch only data for genuinely new symbols. Checkpoint durably after each finished symbol with `python scripts/remote_checkpoint.py --message "chore: grid <SYMBOL>"` (the workflow controller only allows a 30s push, so keep each delta small). One symbol of the 66-pair grid takes ~2.5-3 min and the full candidate check over the 36 surviving cells takes ~4.5 min, so budget ~10 min per symbol.

## Session update (2026-10-20T20:12:00Z)

- Read the batch-22 handoff and reconciled the saved artifacts before touching anything: the prior session had already applied batch 22 (universe **N 217 -> 227**), fetched and validated its ten fixtures and completed the 66-pair grid for all ten, with **14 982 / 14 982 cells** complete and 0 blocked. Nothing was re-run.
- Applied **batch 23** (universe **N 227 -> 237**) from the reviewed saved snapshot `universe/mcap_snapshot_20261020_113004.json` with `--apply-from ... --batch-size 10 --apply`; the dry run and the applied run produced exactly the ten names named in the previous handoff (MTL, DAG, PUNDIX, PUFFER, SQD, WAVES, MLK, TNSR, STRAX, GMT - ranks 228-237). No CoinGecko request was made: the saved pass still held 39 eligible unseen names below the floor, so the 24 h refresh bound did not apply. `universe/last_scan.json` was then refreshed and now reports `universe_n=237`, floor GMT/USDT, 29 eligible unseen names below the floor and the batch-24 candidate list.
- Fetched and validated the ten new hourly fixtures in a single pass with **no failures and no re-queries**: no duplicate timestamps, no missing hours (contiguous 1h grid, max gap 1 h), no invalid OHLC rows, no NaN rows, and price identity `|log(last close / CoinGecko price)|` <= 0.0486 (worst: SQD) - all well inside the 0.20 tolerance. The mandatory ticker-collision check for **MLK (MiL.k), DAG (Constellation), GMT and SQD** passed: all four resolve to the ranked asset (0.0022, 0.0043, 0.0243, 0.0486). Manifest reconciled: 238 rows (237 universe symbols + the pre-fetched CCD file).
- Ran the full 66-pair EMA grid for ranks 228-237, one `--n` invocation per symbol, with a durable remote checkpoint after each symbol. All ten symbols have 66 cells each with a complete artifact set (config, trades, equity, summary). Final state: **15 642 / 15 642 cells** complete, 0 blocked, `next_cell: null`.
- Re-ran `scripts/aggregate_grid.py`: mean net PF 0.4943, median 0.5141, best 2.2274, 12 705 984 trades, 36 cells above net PF 1, 26 exploratory, 15 616 rejected, 0 blocked. Re-ran `scripts/candidate_check.py`: `results/20261020_200452_candidate_check/` - 36/36 rejected, **0 credible candidates**. The above-PF set is unchanged from batch 20; batch 23 contributed no survivor.
- Updated `universe/mcap_expansion_log.md`: added the batch-23 section (selection, fixture coverage table with the ticker-collision, price-scale and history-headroom evidence, grid outcome table), the cumulative state at N=237, the batch-24 candidate list with the ONE/Harmony and SATS warnings, and the batch-23 row in the per-batch coverage table.
- Refreshed this handoff and `INITIAL_TASK_FOR_NEXT_AGENT.md` for batch 24 (SATS, OGN, CETUS, YGG, DODO, ONE, AEVO, SLP, CGPT, WOO; ranks 238-247).
- Tests: `python -m pytest tests/ -q` -> **56 passed**. No code changes in this session.
