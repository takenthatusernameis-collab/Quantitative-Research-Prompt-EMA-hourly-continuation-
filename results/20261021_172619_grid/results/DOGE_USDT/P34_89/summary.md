# EMA Hourly Continuation — DOGE/USDT P34_89

**Symbol:** DOGE/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.6554 |
| net_win_rate | 0.4773 |
| gross_profit_factor | 0.8875 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -2.4199 |
| sortino_ratio | -0.6698 |
| max_drawdown | 0.5363 |
| cagr | -0.2636 |
| net_avg_win | 56.9901 |
| net_avg_loss | -79.4068 |
| avg_hold_time_bars | 12.3973 |
| exposure | 0.2113 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
