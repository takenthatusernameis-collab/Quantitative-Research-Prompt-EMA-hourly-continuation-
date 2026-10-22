# EMA Hourly Continuation — CAKE/USDT P20_26

**Symbol:** CAKE/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1183 |
| net_profit_factor | 0.1591 |
| net_win_rate | 0.3390 |
| gross_profit_factor | 0.7312 |
| gross_win_rate | 0.4167 |
| sharpe_ratio | -15.7005 |
| sortino_ratio | -8.0605 |
| max_drawdown | 1.0000 |
| cagr | -0.9864 |
| net_avg_win | 4.7184 |
| net_avg_loss | -15.2070 |
| avg_hold_time_bars | 2.0811 |
| exposure | 0.1119 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
