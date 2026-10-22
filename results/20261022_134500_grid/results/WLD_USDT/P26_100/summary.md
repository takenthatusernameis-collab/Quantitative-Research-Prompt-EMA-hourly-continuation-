# EMA Hourly Continuation — WLD/USDT P26_100

**Symbol:** WLD/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 599 |
| net_profit_factor | 0.8070 |
| net_win_rate | 0.5242 |
| gross_profit_factor | 1.1088 |
| gross_win_rate | 0.5259 |
| sharpe_ratio | -1.6642 |
| sortino_ratio | -0.5818 |
| max_drawdown | 0.5139 |
| cagr | -0.2397 |
| net_avg_win | 66.2564 |
| net_avg_loss | -90.4571 |
| avg_hold_time_bars | 12.3856 |
| exposure | 0.3372 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
