# EMA Hourly Continuation — PENDLE/USDT P8_50

**Symbol:** PENDLE/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 700 |
| net_profit_factor | 0.7445 |
| net_win_rate | 0.4814 |
| gross_profit_factor | 0.9052 |
| gross_win_rate | 0.4814 |
| sharpe_ratio | -2.3015 |
| sortino_ratio | -0.8685 |
| max_drawdown | 0.6390 |
| cagr | -0.3296 |
| net_avg_win | 54.8033 |
| net_avg_loss | -68.3343 |
| avg_hold_time_bars | 13.2771 |
| exposure | 0.4225 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
