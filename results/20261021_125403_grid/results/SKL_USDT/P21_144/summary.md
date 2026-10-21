# EMA Hourly Continuation — SKL/USDT P21_144

**Symbol:** SKL/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.8513 |
| net_win_rate | 0.5070 |
| gross_profit_factor | 1.0170 |
| gross_win_rate | 0.5070 |
| sharpe_ratio | -0.9452 |
| sortino_ratio | -0.2565 |
| max_drawdown | 0.3809 |
| cagr | -0.1133 |
| net_avg_win | 81.9978 |
| net_avg_loss | -99.0362 |
| avg_hold_time_bars | 34.5292 |
| exposure | 0.5635 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
