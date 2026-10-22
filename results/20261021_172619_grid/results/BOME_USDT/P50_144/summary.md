# EMA Hourly Continuation — BOME/USDT P50_144

**Symbol:** BOME/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.7678 |
| net_win_rate | 0.4845 |
| gross_profit_factor | 0.9145 |
| gross_win_rate | 0.4845 |
| sharpe_ratio | -1.4139 |
| sortino_ratio | -0.3800 |
| max_drawdown | 0.4171 |
| cagr | -0.1613 |
| net_avg_win | 68.6554 |
| net_avg_loss | -84.0399 |
| avg_hold_time_bars | 17.8056 |
| exposure | 0.2873 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
