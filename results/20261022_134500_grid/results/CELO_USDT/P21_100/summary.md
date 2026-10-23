# EMA Hourly Continuation — CELO/USDT P21_100

**Symbol:** CELO/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 577 |
| net_profit_factor | 0.7232 |
| net_win_rate | 0.4974 |
| gross_profit_factor | 1.0583 |
| gross_win_rate | 0.5095 |
| sharpe_ratio | -2.6327 |
| sortino_ratio | -0.8929 |
| max_drawdown | 0.6703 |
| cagr | -0.3434 |
| net_avg_win | 59.5464 |
| net_avg_loss | -81.4818 |
| avg_hold_time_bars | 17.3726 |
| exposure | 0.4536 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
