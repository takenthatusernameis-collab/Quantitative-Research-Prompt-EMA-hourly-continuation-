# EMA Hourly Continuation — SQD/USDT P8_200

**Symbol:** SQD/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.7806 |
| net_win_rate | 0.4966 |
| gross_profit_factor | 0.9746 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -1.4990 |
| sortino_ratio | -0.4542 |
| max_drawdown | 0.4369 |
| cagr | -0.1931 |
| net_avg_win | 65.6796 |
| net_avg_loss | -83.0101 |
| avg_hold_time_bars | 35.2460 |
| exposure | 0.7339 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
