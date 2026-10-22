# EMA Hourly Continuation — MERL/USDT P55_100

**Symbol:** MERL/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.7189 |
| net_win_rate | 0.4786 |
| gross_profit_factor | 0.8907 |
| gross_win_rate | 0.4786 |
| sharpe_ratio | -1.7897 |
| sortino_ratio | -0.4789 |
| max_drawdown | 0.4595 |
| cagr | -0.1977 |
| net_avg_win | 64.5416 |
| net_avg_loss | -82.4160 |
| avg_hold_time_bars | 8.7835 |
| exposure | 0.1405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
