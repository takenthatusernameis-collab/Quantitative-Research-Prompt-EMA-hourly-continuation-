# EMA Hourly Continuation — ROSE/USDT P26_34

**Symbol:** ROSE/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 205 |
| net_profit_factor | 0.7845 |
| net_win_rate | 0.5220 |
| gross_profit_factor | 1.0893 |
| gross_win_rate | 0.5220 |
| sharpe_ratio | -1.0264 |
| sortino_ratio | -0.2120 |
| max_drawdown | 0.2511 |
| cagr | -0.0921 |
| net_avg_win | 73.3022 |
| net_avg_loss | -102.0176 |
| avg_hold_time_bars | 4.6293 |
| exposure | 0.0431 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
