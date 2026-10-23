# EMA Hourly Continuation — CELR/USDT P26_144

**Symbol:** CELR/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.5952 |
| net_win_rate | 0.4487 |
| gross_profit_factor | 0.8528 |
| gross_win_rate | 0.4608 |
| sharpe_ratio | -3.6185 |
| sortino_ratio | -1.1338 |
| max_drawdown | 0.7532 |
| cagr | -0.4138 |
| net_avg_win | 48.8046 |
| net_avg_loss | -66.7313 |
| avg_hold_time_bars | 22.5070 |
| exposure | 0.5062 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
