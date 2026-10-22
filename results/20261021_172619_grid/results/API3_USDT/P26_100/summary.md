# EMA Hourly Continuation — API3/USDT P26_100

**Symbol:** API3/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.8014 |
| net_win_rate | 0.5022 |
| gross_profit_factor | 1.0074 |
| gross_win_rate | 0.5022 |
| sharpe_ratio | -1.4917 |
| sortino_ratio | -0.4546 |
| max_drawdown | 0.4382 |
| cagr | -0.1893 |
| net_avg_win | 72.8180 |
| net_avg_loss | -91.6691 |
| avg_hold_time_bars | 17.0133 |
| exposure | 0.3495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
