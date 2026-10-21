# EMA Hourly Continuation — ICP/USDT P26_144

**Symbol:** ICP/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.8184 |
| net_win_rate | 0.5041 |
| gross_profit_factor | 1.0016 |
| gross_win_rate | 0.5041 |
| sharpe_ratio | -1.1409 |
| sortino_ratio | -0.3112 |
| max_drawdown | 0.3377 |
| cagr | -0.1348 |
| net_avg_win | 75.0713 |
| net_avg_loss | -93.2570 |
| avg_hold_time_bars | 28.4931 |
| exposure | 0.4701 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
