# EMA Hourly Continuation — MLK/USDT P26_55

**Symbol:** MLK/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1171 |
| net_profit_factor | 0.2289 |
| net_win_rate | 0.2647 |
| gross_profit_factor | 0.5542 |
| gross_win_rate | 0.2852 |
| sharpe_ratio | -16.1086 |
| sortino_ratio | -8.0412 |
| max_drawdown | 1.0000 |
| cagr | -0.9838 |
| net_avg_win | 9.5748 |
| net_avg_loss | -15.0614 |
| avg_hold_time_bars | 3.8155 |
| exposure | 0.2022 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
