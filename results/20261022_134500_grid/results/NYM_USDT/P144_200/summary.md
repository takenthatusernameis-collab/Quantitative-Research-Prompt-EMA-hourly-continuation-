# EMA Hourly Continuation — NYM/USDT P144_200

**Symbol:** NYM/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.1689 |
| net_win_rate | 0.3189 |
| gross_profit_factor | 0.4880 |
| gross_win_rate | 0.3549 |
| sharpe_ratio | -8.8761 |
| sortino_ratio | -2.6503 |
| max_drawdown | 0.9714 |
| cagr | -0.7572 |
| net_avg_win | 14.8425 |
| net_avg_loss | -41.1553 |
| avg_hold_time_bars | 6.3453 |
| exposure | 0.1203 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
