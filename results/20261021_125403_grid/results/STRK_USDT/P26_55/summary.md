# EMA Hourly Continuation — STRK/USDT P26_55

**Symbol:** STRK/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.7170 |
| net_win_rate | 0.4811 |
| gross_profit_factor | 0.9267 |
| gross_win_rate | 0.4811 |
| sharpe_ratio | -2.1078 |
| sortino_ratio | -0.6002 |
| max_drawdown | 0.4986 |
| cagr | -0.2404 |
| net_avg_win | 66.1348 |
| net_avg_loss | -85.5255 |
| avg_hold_time_bars | 7.0957 |
| exposure | 0.1280 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
