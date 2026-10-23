# EMA Hourly Continuation — CETUS/USDT P34_50

**Symbol:** CETUS/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 911 |
| net_profit_factor | 0.4697 |
| net_win_rate | 0.4490 |
| gross_profit_factor | 0.9115 |
| gross_win_rate | 0.4687 |
| sharpe_ratio | -7.6936 |
| sortino_ratio | -3.2760 |
| max_drawdown | 0.9836 |
| cagr | -0.8022 |
| net_avg_win | 21.2935 |
| net_avg_loss | -36.9346 |
| avg_hold_time_bars | 2.8145 |
| exposure | 0.1160 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
