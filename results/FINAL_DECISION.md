# Final Decision — EMA Hourly Continuation

## Program status — 2026-10-20T23:47Z (supersedes the 2026-10-19 baseline decision)

Strategy: EMA hourly continuation (PROMPT.md). Universe: **266 symbols** ranked by
market cap descending, full EMA period grid (**66 pairs** from
`{8, 12, 20, 21, 26, 34, 50, 55, 89, 100, 144, 200}`), hourly KuCoin OHLCV, net of
costs (10 bps taker + 2 bps slippage per side).

**Decision: no credible edge. The strategy is rejected on the evidence to date,
and the program keeps expanding the universe until the expansion is impossible
(PROMPT.md §2.1) — a negative result is never a program stop.**

| Gate | Result |
|---|---|
| Grid cells evaluated | **17 556 / 17 556** (266 symbols x 66 pairs), 0 blocked |
| Labels | 17 530 rejected, 26 exploratory, **0 credible candidates** |
| Cells with full-sample net PF > 1 | **36 / 17 556 = 0.21 %** against a ~50 % no-edge null (excess -49.8 %) |
| Mean / median net PF (per cell) | 0.4993 / 0.5205 |
| Pooled net PF (trade-level) | **0.5224** over 14 240 827 trades |
| Best cell | BABYDOGE/USDT P50_55, net PF 2.2274 — rejected, 0 out-of-sample trades |

### Robustness legs (PROMPT.md §3.3)

- **Out-of-sample + 2x cost stress** (`scripts/candidate_check.py`): all 36
  net-PF > 1 cells rejected; 0 credible candidates. Artifact:
  `results/20261020_233737_candidate_check/summary.md`.
- **Drop the N largest market caps** (`scripts/robustness_pooled.py`): pooled net
  PF 0.5224 (all) -> 0.5248 (minus top 5) -> 0.5263 (top 10) -> 0.5280 (top 20)
  -> 0.5303 (top 50). The result does not depend on the largest names.
- **Rank buckets**: 1-10 0.4083, 11-50 0.5037, 51-100 0.5188, 101-200 0.5360,
  201+ 0.5302. Every bucket is below 1.0.
- **Subperiod stability** (4 equal-time slices per cell): of the 36 net-PF > 1
  cells, 31 are fragile across slices, 4 are too thin to judge, and 1
  (BABYDOGE/USDT P50_89) is stable but has 0 out-of-sample trades. Artifact:
  `results/20261020_235449_robustness/summary.md`.
- **Conservative same-bar exit** (stop first) is the registered baseline of every
  cell in the grid.

### Recommendation

- No live trading, no promotion to production: nothing in 17 556 grid cells
  survives the out-of-sample and cost-stress gates.
- Keep expanding the universe in market-cap descending order (§2.1) and keep
  running the full 66-pair grid per symbol. The next expansion is blocked only
  by the 24 h market-cap refresh bound, which opens **2026-10-21T11:30:04Z**.

---

## Baseline study (2026-10-19, 5 symbols) — historical record

Date: 2026-10-19
Strategy: EMA hourly continuation (PROMPT.md)
Sample: Real hourly OHLCV only (BTC/USDT 25k, ETH/SOL/BNB/XRP 22k; UTC). Data in `data/fixtures/`, `fetch_manifest.json`.

## Acceptance OOS (reproduced)
- Command: `PYTHONPATH=. python scripts/oos_pooled.py --test-fraction 0.35 --rr 1.5 --min-risk-atr --atr-threshold 0.75 --n 5`
- Results: `results/20261019_064215_oos_pooled/`
- Pooled: 666 trades, net PF=0.6890, net Sharpe=-1.9443, max DD=0.6663
- Per-symbol: BTC 124 (PF 0.6860, Sharpe -0.9004); ETH 119 (PF 0.7861, Sharpe -1.8710); SOL 132 (PF 0.8792, Sharpe -1.1395); BNB 150 (PF 0.6955, Sharpe -2.8661); XRP 141 (PF 0.8006, Sharpe -1.8986)

## Robustness
- Cost stress (2x, full sample): base 0.6906 → stress 0.4691; Sharpe 0.8550 → -0.7038; max DD 1.89 → 4.09
- ATR grid (OOS): atr 0.5 (826 tr, PF 0.6354, Sharpe -2.1419), atr 1.0 (517 tr, PF 0.6501, Sharpe -2.0586), atr 1.5 (302 tr, PF 0.7922, Sharpe -1.2193)
- Same-bar exit: conservative vs aggressive TP-first — negligible delta (PF 0.6890→0.6952, Sharpe -1.9443→-1.9169)
- Stricter trend: no-op; same metrics

## Decision
**REJECTED**. Strategy fails on OOS net-of-costs (negative Sharpe, PF<1, substantial max drawdown). Larger real sample did not improve profitability; cost stress materially worsens results; no tested robustness variant reaches profitability. Adequate sample size (666 pooled trades, 22k–25k bars/symbol).

## Recommendation
- No live trading. Do not promote to production.
- Do not continue parameter tuning of this baseline. Only pursue if a new, pre-specified hypothesis is formulated (with clear theoretical rationale and falsifiable acceptance criteria) before testing.

> This 5-symbol section is the historical record of the first study. It did not
> account for the mandatory expanding-universe rule of PROMPT.md §2.1, so the
> program continued to larger, lower-market-cap names; the decision above is
> unchanged in substance and is now supported by 17 556 grid cells instead of
> 666 pooled trades.
