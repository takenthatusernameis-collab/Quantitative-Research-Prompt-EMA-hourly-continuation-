# EMA Hourly Continuation — AXS/USDT P55_100

**Symbol:** AXS/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.7721 |
| net_win_rate | 0.5170 |
| gross_profit_factor | 1.0637 |
| gross_win_rate | 0.5170 |
| sharpe_ratio | -1.4351 |
| sortino_ratio | -0.3707 |
| max_drawdown | 0.4053 |
| cagr | -0.1565 |
| net_avg_win | 70.7991 |
| net_avg_loss | -98.1651 |
| avg_hold_time_bars | 8.1238 |
| exposure | 0.1187 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
