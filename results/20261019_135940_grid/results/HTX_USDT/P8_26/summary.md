# EMA Hourly Continuation — HTX/USDT P8_26

**Symbol:** HTX/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1643 |
| net_profit_factor | 0.1340 |
| net_win_rate | 0.2599 |
| gross_profit_factor | 0.5073 |
| gross_win_rate | 0.3421 |
| sharpe_ratio | -21.9087 |
| sortino_ratio | -13.5220 |
| max_drawdown | 1.0000 |
| cagr | -0.9994 |
| net_avg_win | 3.6243 |
| net_avg_loss | -9.4963 |
| avg_hold_time_bars | 4.2240 |
| exposure | 0.3141 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
