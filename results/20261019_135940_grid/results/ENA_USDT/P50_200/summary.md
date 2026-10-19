# EMA Hourly Continuation — ENA/USDT P50_200

**Symbol:** ENA/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.6486 |
| net_win_rate | 0.4598 |
| gross_profit_factor | 0.8415 |
| gross_win_rate | 0.4626 |
| sharpe_ratio | -2.5411 |
| sortino_ratio | -0.6788 |
| max_drawdown | 0.5636 |
| cagr | -0.2734 |
| net_avg_win | 61.3381 |
| net_avg_loss | -80.5023 |
| avg_hold_time_bars | 21.8116 |
| exposure | 0.3579 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
