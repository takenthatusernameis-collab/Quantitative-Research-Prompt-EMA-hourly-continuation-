# EMA Hourly Continuation — JUP/USDT P55_200

**Symbol:** JUP/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.5436 |
| net_win_rate | 0.4509 |
| gross_profit_factor | 0.8040 |
| gross_win_rate | 0.4556 |
| sharpe_ratio | -3.7353 |
| sortino_ratio | -1.0805 |
| max_drawdown | 0.7476 |
| cagr | -0.4068 |
| net_avg_win | 45.0776 |
| net_avg_loss | -68.1084 |
| avg_hold_time_bars | 15.5678 |
| exposure | 0.3029 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
