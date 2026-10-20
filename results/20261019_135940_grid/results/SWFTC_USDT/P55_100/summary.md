# EMA Hourly Continuation — SWFTC/USDT P55_100

**Symbol:** SWFTC/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 643 |
| net_profit_factor | 0.4761 |
| net_win_rate | 0.4230 |
| gross_profit_factor | 0.8923 |
| gross_win_rate | 0.4417 |
| sharpe_ratio | -6.9598 |
| sortino_ratio | -2.4862 |
| max_drawdown | 0.9582 |
| cagr | -0.7166 |
| net_avg_win | 31.9978 |
| net_avg_loss | -49.2773 |
| avg_hold_time_bars | 4.5350 |
| exposure | 0.1325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
