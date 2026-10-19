# EMA Hourly Continuation — IOTA/USDT P34_100

**Symbol:** IOTA/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.5238 |
| net_win_rate | 0.4475 |
| gross_profit_factor | 0.8457 |
| gross_win_rate | 0.4521 |
| sharpe_ratio | -5.2772 |
| sortino_ratio | -1.8981 |
| max_drawdown | 0.9057 |
| cagr | -0.6016 |
| net_avg_win | 33.7034 |
| net_avg_loss | -52.1131 |
| avg_hold_time_bars | 8.6849 |
| exposure | 0.2594 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
