# EMA Hourly Continuation — BIGTIME/USDT P21_34

**Symbol:** BIGTIME/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.6277 |
| net_win_rate | 0.4814 |
| gross_profit_factor | 0.8974 |
| gross_win_rate | 0.4814 |
| sharpe_ratio | -2.9356 |
| sortino_ratio | -0.8702 |
| max_drawdown | 0.6439 |
| cagr | -0.3273 |
| net_avg_win | 51.4913 |
| net_avg_loss | -76.1449 |
| avg_hold_time_bars | 5.5512 |
| exposure | 0.1080 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
