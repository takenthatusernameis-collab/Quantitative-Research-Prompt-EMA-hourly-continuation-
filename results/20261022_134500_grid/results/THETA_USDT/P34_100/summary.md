# EMA Hourly Continuation — THETA/USDT P34_100

**Symbol:** THETA/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 654 |
| net_profit_factor | 0.5773 |
| net_win_rate | 0.4679 |
| gross_profit_factor | 0.9164 |
| gross_win_rate | 0.4771 |
| sharpe_ratio | -4.4618 |
| sortino_ratio | -1.6096 |
| max_drawdown | 0.8642 |
| cagr | -0.5374 |
| net_avg_win | 38.1914 |
| net_avg_loss | -58.1718 |
| avg_hold_time_bars | 8.2095 |
| exposure | 0.2440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
