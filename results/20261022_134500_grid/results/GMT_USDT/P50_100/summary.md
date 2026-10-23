# EMA Hourly Continuation — GMT/USDT P50_100

**Symbol:** GMT/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 641 |
| net_profit_factor | 0.5571 |
| net_win_rate | 0.4571 |
| gross_profit_factor | 0.9656 |
| gross_win_rate | 0.4649 |
| sharpe_ratio | -5.3850 |
| sortino_ratio | -1.9288 |
| max_drawdown | 0.9098 |
| cagr | -0.6073 |
| net_avg_win | 38.8284 |
| net_avg_loss | -58.6790 |
| avg_hold_time_bars | 5.6661 |
| exposure | 0.1651 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
