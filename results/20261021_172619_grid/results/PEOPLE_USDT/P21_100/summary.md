# EMA Hourly Continuation — PEOPLE/USDT P21_100

**Symbol:** PEOPLE/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.8308 |
| net_win_rate | 0.5047 |
| gross_profit_factor | 0.9976 |
| gross_win_rate | 0.5047 |
| sharpe_ratio | -1.1146 |
| sortino_ratio | -0.3279 |
| max_drawdown | 0.3896 |
| cagr | -0.1417 |
| net_avg_win | 73.4038 |
| net_avg_loss | -90.0380 |
| avg_hold_time_bars | 23.6014 |
| exposure | 0.4528 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
