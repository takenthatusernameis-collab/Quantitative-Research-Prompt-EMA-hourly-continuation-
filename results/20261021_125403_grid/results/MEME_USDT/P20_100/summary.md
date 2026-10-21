# EMA Hourly Continuation — MEME/USDT P20_100

**Symbol:** MEME/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.8161 |
| net_win_rate | 0.5010 |
| gross_profit_factor | 1.0065 |
| gross_win_rate | 0.5010 |
| sharpe_ratio | -1.4878 |
| sortino_ratio | -0.4681 |
| max_drawdown | 0.4791 |
| cagr | -0.1958 |
| net_avg_win | 77.2655 |
| net_avg_loss | -95.0702 |
| avg_hold_time_bars | 19.8571 |
| exposure | 0.4360 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
