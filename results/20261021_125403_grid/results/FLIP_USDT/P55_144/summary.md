# EMA Hourly Continuation — FLIP/USDT P55_144

**Symbol:** FLIP/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 258 |
| net_profit_factor | 0.5720 |
| net_win_rate | 0.4302 |
| gross_profit_factor | 0.7893 |
| gross_win_rate | 0.4341 |
| sharpe_ratio | -3.0262 |
| sortino_ratio | -0.6824 |
| max_drawdown | 0.5726 |
| cagr | -0.2768 |
| net_avg_win | 67.0466 |
| net_avg_loss | -88.5041 |
| avg_hold_time_bars | 21.7558 |
| exposure | 0.2551 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
