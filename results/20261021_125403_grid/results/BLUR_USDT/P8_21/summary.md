# EMA Hourly Continuation — BLUR/USDT P8_21

**Symbol:** BLUR/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 650 |
| net_profit_factor | 0.6602 |
| net_win_rate | 0.4708 |
| gross_profit_factor | 0.9061 |
| gross_win_rate | 0.4708 |
| sharpe_ratio | -3.5926 |
| sortino_ratio | -1.3059 |
| max_drawdown | 0.7841 |
| cagr | -0.4507 |
| net_avg_win | 49.4910 |
| net_avg_loss | -66.6798 |
| avg_hold_time_bars | 5.7015 |
| exposure | 0.1677 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
