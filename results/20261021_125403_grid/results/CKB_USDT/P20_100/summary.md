# EMA Hourly Continuation — CKB/USDT P20_100

**Symbol:** CKB/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.8215 |
| net_win_rate | 0.5084 |
| gross_profit_factor | 1.0298 |
| gross_win_rate | 0.5084 |
| sharpe_ratio | -1.3814 |
| sortino_ratio | -0.4323 |
| max_drawdown | 0.4193 |
| cagr | -0.1818 |
| net_avg_win | 75.2828 |
| net_avg_loss | -94.7757 |
| avg_hold_time_bars | 18.7395 |
| exposure | 0.4055 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
