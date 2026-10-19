# EMA Hourly Continuation — RAY/USDT P8_100

**Symbol:** RAY/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 687 |
| net_profit_factor | 0.6839 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 0.9641 |
| gross_win_rate | 0.4964 |
| sharpe_ratio | -2.9611 |
| sortino_ratio | -1.0927 |
| max_drawdown | 0.7532 |
| cagr | -0.4045 |
| net_avg_win | 47.2970 |
| net_avg_loss | -65.0548 |
| avg_hold_time_bars | 20.5066 |
| exposure | 0.6404 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
