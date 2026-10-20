# EMA Hourly Continuation — SWFTC/USDT P21_26

**Symbol:** SWFTC/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1109 |
| net_profit_factor | 0.1315 |
| net_win_rate | 0.3093 |
| gross_profit_factor | 0.4776 |
| gross_win_rate | 0.3490 |
| sharpe_ratio | -15.9119 |
| sortino_ratio | -7.7790 |
| max_drawdown | 1.0000 |
| cagr | -0.9877 |
| net_avg_win | 4.4140 |
| net_avg_loss | -15.0311 |
| avg_hold_time_bars | 2.0730 |
| exposure | 0.1045 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
