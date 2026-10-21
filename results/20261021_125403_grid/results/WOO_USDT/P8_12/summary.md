# EMA Hourly Continuation — WOO/USDT P8_12

**Symbol:** WOO/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.6995 |
| net_win_rate | 0.4939 |
| gross_profit_factor | 1.0209 |
| gross_win_rate | 0.4963 |
| sharpe_ratio | -2.5540 |
| sortino_ratio | -0.7415 |
| max_drawdown | 0.5859 |
| cagr | -0.2885 |
| net_avg_win | 66.2330 |
| net_avg_loss | -92.3946 |
| avg_hold_time_bars | 4.2592 |
| exposure | 0.0792 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
