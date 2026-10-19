# EMA Hourly Continuation — KMNO/USDT P21_100

**Symbol:** KMNO/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 557 |
| net_profit_factor | 0.6297 |
| net_win_rate | 0.4596 |
| gross_profit_factor | 0.8955 |
| gross_win_rate | 0.4668 |
| sharpe_ratio | -3.8535 |
| sortino_ratio | -1.2868 |
| max_drawdown | 0.7845 |
| cagr | -0.4605 |
| net_avg_win | 51.9882 |
| net_avg_loss | -70.2155 |
| avg_hold_time_bars | 15.6140 |
| exposure | 0.4015 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
