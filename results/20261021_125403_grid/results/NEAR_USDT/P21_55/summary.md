# EMA Hourly Continuation — NEAR/USDT P21_55

**Symbol:** NEAR/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.7497 |
| net_win_rate | 0.4874 |
| gross_profit_factor | 0.9463 |
| gross_win_rate | 0.4874 |
| sharpe_ratio | -1.8906 |
| sortino_ratio | -0.5637 |
| max_drawdown | 0.5098 |
| cagr | -0.2290 |
| net_avg_win | 67.7525 |
| net_avg_loss | -85.9170 |
| avg_hold_time_bars | 9.2368 |
| exposure | 0.1826 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
