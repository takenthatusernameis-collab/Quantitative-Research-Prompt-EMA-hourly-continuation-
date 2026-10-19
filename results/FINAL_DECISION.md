# Final Decision — EMA Hourly Continuation

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
