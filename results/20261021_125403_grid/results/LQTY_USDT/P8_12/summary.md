# EMA Hourly Continuation — LQTY/USDT P8_12

**Symbol:** LQTY/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 414 |
| net_profit_factor | 0.5541 |
| net_win_rate | 0.4444 |
| gross_profit_factor | 0.8180 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -3.9281 |
| sortino_ratio | -1.1403 |
| max_drawdown | 0.7456 |
| cagr | -0.4074 |
| net_avg_win | 49.4843 |
| net_avg_loss | -71.4508 |
| avg_hold_time_bars | 4.5145 |
| exposure | 0.0846 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
