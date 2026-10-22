# EMA Hourly Continuation — BAND/USDT P34_55

**Symbol:** BAND/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.6796 |
| net_win_rate | 0.5021 |
| gross_profit_factor | 1.0122 |
| gross_win_rate | 0.5062 |
| sharpe_ratio | -2.7344 |
| sortino_ratio | -0.8650 |
| max_drawdown | 0.6498 |
| cagr | -0.3263 |
| net_avg_win | 54.8409 |
| net_avg_loss | -81.3595 |
| avg_hold_time_bars | 5.8560 |
| exposure | 0.1288 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
