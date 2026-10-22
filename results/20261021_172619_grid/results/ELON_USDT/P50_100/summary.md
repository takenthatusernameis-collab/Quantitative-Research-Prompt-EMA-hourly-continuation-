# EMA Hourly Continuation — ELON/USDT P50_100

**Symbol:** ELON/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.6799 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 0.9126 |
| gross_win_rate | 0.4847 |
| sharpe_ratio | -2.0436 |
| sortino_ratio | -0.5283 |
| max_drawdown | 0.4750 |
| cagr | -0.2136 |
| net_avg_win | 60.9075 |
| net_avg_loss | -84.2499 |
| avg_hold_time_bars | 8.5245 |
| exposure | 0.1263 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
