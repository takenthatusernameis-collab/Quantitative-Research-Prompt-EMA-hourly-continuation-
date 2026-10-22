# EMA Hourly Continuation — MANA/USDT P26_89

**Symbol:** MANA/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 696 |
| net_profit_factor | 0.6325 |
| net_win_rate | 0.4612 |
| gross_profit_factor | 1.0400 |
| gross_win_rate | 0.4698 |
| sharpe_ratio | -5.4977 |
| sortino_ratio | -2.0264 |
| max_drawdown | 0.9285 |
| cagr | -0.6356 |
| net_avg_win | 49.3596 |
| net_avg_loss | -66.8047 |
| avg_hold_time_bars | 10.0316 |
| exposure | 0.3174 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
