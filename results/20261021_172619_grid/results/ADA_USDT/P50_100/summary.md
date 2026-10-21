# EMA Hourly Continuation — ADA/USDT P50_100

**Symbol:** ADA/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.7040 |
| net_win_rate | 0.4985 |
| gross_profit_factor | 0.9557 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -1.7825 |
| sortino_ratio | -0.4650 |
| max_drawdown | 0.4350 |
| cagr | -0.1921 |
| net_avg_win | 59.7829 |
| net_avg_loss | -84.4059 |
| avg_hold_time_bars | 9.1692 |
| exposure | 0.1380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
