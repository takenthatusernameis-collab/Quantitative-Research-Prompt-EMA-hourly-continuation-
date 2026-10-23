# EMA Hourly Continuation — CSPR/USDT P8_100

**Symbol:** CSPR/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 912 |
| net_profit_factor | 0.4574 |
| net_win_rate | 0.4112 |
| gross_profit_factor | 0.7271 |
| gross_win_rate | 0.4178 |
| sharpe_ratio | -7.1113 |
| sortino_ratio | -3.0084 |
| max_drawdown | 0.9754 |
| cagr | -0.7691 |
| net_avg_win | 21.9124 |
| net_avg_loss | -33.4547 |
| avg_hold_time_bars | 14.9792 |
| exposure | 0.6210 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
