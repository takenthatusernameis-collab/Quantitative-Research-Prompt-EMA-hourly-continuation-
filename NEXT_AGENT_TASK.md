# NEXT AGENT TASK

## Current state (verified against the saved artifacts, 2026-10-20T10:15:00Z)

**Program status: `AWAITING_NEW_ELIGIBLE_CANDIDATES`, not permanently complete.** Batch 17 completed the universe expansion from N=167 to N=177. The most recent recorded universe is `universe/mcap_rank.json`, snapshot `mcap_snapshot_20261020_082835` (CoinGecko, retrieved 2026-10-20T08:28:35Z). Batch 17 appended XYO, POLYX, AURORA, POPCAT, REQ, LSK, MASK, ZIL, ANKR and BOME in descending market-cap order. The current floor is BOME at approximately USD 41.20M in that snapshot.

- Grid: **11,682 / 11,682 cells complete** in `results/20261019_135940_grid/` (177 symbols × 66 EMA pairs); 0 blocked.
- Decision count: **11,657 rejected**, 25 exploratory at the initial scan, and **0 credible candidates** after robustness checks.
- Pooled, full-sample net of costs (10 bps taker + 2 bps slippage per side): mean net profit factor **0.4917**, median **0.5112**, best in-sample PF **2.2274** (BABYDOGE/USDT P50_55; rejected, zero OOS trades), **9,567,069 trades**.
- Cells with full-sample net PF > 1: **35 / 11,682 (0.30%)**. All 35 failed the required OOS and 2×-cost checks. The OOS window is the trailing 35% of each symbol's bars. No credible cell has been found.
- Candidate-check artifact: `results/20261020_094859_candidate_check/summary.md`. Requirements for credibility remain: OOS net PF > 1, OOS Sharpe > 0, at least 30 OOS trades, and PF > 1 under 2× fees/slippage.
- Tests last recorded: `python -m pytest tests/ -q` → **56 passed** (verified 2026-10-20T12:21:59Z).- Latest expansion added: `universe/mcap_rank.json` N=177, snapshot `mcap_snapshot_20261020_082835`.

**Fresh ranking scan (2026-10-20T10:02:36Z):** Retrieved `universe/mcap_snapshot_20261020_100236.json` (pages 1–5, 500 entries). Checked all eligible (tradable on KuCoin spot USDT, no exclusion) entries not in the working universe (N=177). Found **GAS/USDT (rank 318, mcap ~80.37M)** which is above the current BOME floor (~41.20M). **No eligible unseen assets below the current floor.** The symbols below BOME in the prior snapshot (e.g. CCD, CSPR, API3, NOT, MOG, PEOPLE, etc.) were not present as eligible tradable pairs in the fresh snapshot or had dropped below eligibility. Evidence: full scan of pages 1–5 complete; no candidates with mcap < 41.20M satisfy KuCoin spot USDT tradability and history filters.

The prior handoff records that a scan of CoinGecko pages 4–5 found no currently eligible unseen assets below the existing market-cap floor. That is evidence about that checked snapshot and the filters at that time, **not proof that future snapshots can never produce eligible assets**. Do not fabricate a batch, and do not mark the long-running research program permanently complete solely because one full scan found no candidates.

**State:** `AWAITING_NEW_ELIGIBLE_CANDIDATES`. **Next eligible refresh:** no earlier than 2026-10-21T10:02:36Z (>= 24h after the 2026-10-20T10:02:36Z scan). Do **not** re-scan more frequently than once per 24h while in this state.

## Required next action — continue market-cap expansion safely

1. **Reconcile state first.** Read this handoff, `PROMPT.md` §2.1, `universe/mcap_rank.json`, the latest snapshot, `universe/mcap_expansion_log.md`, the grid `progress.json`, and the latest candidate-check artifact. Determine the timestamp and scope of the most recent complete ranking scan. Do not repeat a completed scan or rerun finished grid cells.
2. **Bound empty-scan refreshes.** When the latest complete scan found zero eligible new names, avoid re-querying CoinGecko on every five-minute agent activation. Re-run the full ranking eligibility scan no more than once per 24 hours unless a genuinely new ranking snapshot has already been made available by another legitimate process. Record the timestamp, page coverage, exclusions and evidence. Continue independent code/test/research-quality work between refreshes. This is a temporary waiting state, not permanent program completion.
3. **On the next due refresh, retrieve a fresh descending market-cap snapshot** using the existing script (start with `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 5 --batch-size 10` as a dry run). Inspect the timestamped snapshot it writes and the exact candidate/exclusion results. Extend the page count only when needed to complete the ranking pass below the current floor; obey bounded retries and respect provider rate limits.
4. **If eligible new symbols are found**, select up to the next 10 candidates that are (a) not already in the working universe, (b) strictly below the current floor in the new snapshot, (c) tradable on the data-layer exchange as the same underlying asset, and (d) pass the registered minimum-history and other filters. Preserve append-only global ordering: never remove or reorder existing rows. Apply only from the reviewed saved snapshot: `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --apply-from universe/mcap_snapshot_<TS>.json --batch-size 10 --apply`.
5. Fetch and validate the new hourly OHLCV fixtures with `PYTHONPATH=. python3 scripts/fetch_kucoin.py --target-bars 22000 --symbols <new symbols>`, then reconcile provenance with `PYTHONPATH=. python3 scripts/fetch_kucoin.py --reconcile-manifest`. A transient API error is not proof of ineligibility: re-query a failed symbol as the existing prompt specifies before excluding it. Record coverage, gaps, duplicates, price/ticker identity and all exclusion reasons.
6. Run the **entire 66-pair grid for each newly appended symbol** in strict market-cap order, checkpointing one symbol at a time. Resume the existing run; do not overwrite completed cells:
   `PYTHONPATH=. python3 scripts/run_grid.py --n <rank-in-working-universe> --resume results/20261019_135940_grid --note "universe expansion batch 18: N 177 -> 187 (<SYMBOL>/USDT, 66-pair EMA grid)"`
   After each symbol, checkpoint its result as in the previous batches. Then run `scripts/aggregate_grid.py --run results/20261019_135940_grid` and `scripts/candidate_check.py --run results/20261019_135940_grid`; update the expansion log, progress summary and this handoff with the actual outcome.
7. **If a full fresh ranking pass again yields zero eligible names**, persist a truthful `AWAITING_NEW_ELIGIBLE_CANDIDATES` state with evidence and the next eligible refresh time (>=24h out). Do not invent names, repeatedly hit providers, change the strategy baseline, or call a candidate credible on in-sample metrics. On a later due refresh, repeat the scan and continue if the opportunity set has changed.

## Session update (2026-10-20T12:21:59Z)

- Reconciled state: still `AWAITING_NEW_ELIGIBLE_CANDIDATES`. No new eligible names; 24h refresh not due until 2026-10-21T10:02:36Z.
- Independent verification performed: `python -m pytest tests/ -q` → 56 passed. No code changes.
- Universe remains N=177, floor BOME ~USD 41.20M. Grid complete 11,682/11,682, 0 credible candidates.
- Next eligible refresh: no earlier than 2026-10-21T10:02:36Z.

- Keep the universe append-only and strictly market-cap descending; add only new eligible symbols below the existing floor.
- Never stop merely because the grid or a batch produced no edge. No eligible names *in a particular checked snapshot* means wait for a later bounded refresh, not permanent closure.
- Never lower data-history or liquidity requirements to force expansion. Distinguish a genuinely absent pair/history from a transient API error or an incomplete ranking scan.
- Never promote an in-sample winner without passing the preregistered OOS and doubled-cost gates. Preserve every prior result, candidate rejection and provenance record.
- Keep the registered baseline and 66-pair EMA grid unchanged unless a separately preregistered mutation is authorized.
- Run `python -m pytest tests/ -q` after code changes and report the exact results.

## Environment

Use `PYTHONPATH=. python3 scripts/...` from the repository root. Available data fixtures and all prior result artifacts are reusable; fetch only data for genuinely new symbols.
