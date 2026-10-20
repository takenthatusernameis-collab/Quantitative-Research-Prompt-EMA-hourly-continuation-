# EMA Hourly Continuation — SQD/USDT P21_100

**Symbol:** SQD/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 659 |
| net_profit_factor | 0.7229 |
| net_win_rate | 0.4901 |
| gross_profit_factor | 1.0032 |
| gross_win_rate | 0.4977 |
| sharpe_ratio | -2.8305 |
| sortino_ratio | -1.0406 |
| max_drawdown | 0.7127 |
| cagr | -0.3908 |
| net_avg_win | 56.5277 |
| net_avg_loss | -75.1724 |
| avg_hold_time_bars | 12.6343 |
| exposure | 0.3914 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
