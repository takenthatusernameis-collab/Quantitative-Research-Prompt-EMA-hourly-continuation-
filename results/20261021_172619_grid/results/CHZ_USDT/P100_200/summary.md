# EMA Hourly Continuation — CHZ/USDT P100_200

**Symbol:** CHZ/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 242 |
| net_profit_factor | 0.7505 |
| net_win_rate | 0.4917 |
| gross_profit_factor | 0.9513 |
| gross_win_rate | 0.4917 |
| sharpe_ratio | -1.3212 |
| sortino_ratio | -0.2940 |
| max_drawdown | 0.3082 |
| cagr | -0.1271 |
| net_avg_win | 73.1005 |
| net_avg_loss | -94.2365 |
| avg_hold_time_bars | 14.7231 |
| exposure | 0.1620 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
