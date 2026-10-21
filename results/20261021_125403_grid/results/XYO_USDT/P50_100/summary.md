# EMA Hourly Continuation — XYO/USDT P50_100

**Symbol:** XYO/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.6142 |
| net_win_rate | 0.4558 |
| gross_profit_factor | 0.8642 |
| gross_win_rate | 0.4558 |
| sharpe_ratio | -3.1725 |
| sortino_ratio | -0.8727 |
| max_drawdown | 0.6421 |
| cagr | -0.3321 |
| net_avg_win | 59.8053 |
| net_avg_loss | -81.5471 |
| avg_hold_time_bars | 10.1260 |
| exposure | 0.1709 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
