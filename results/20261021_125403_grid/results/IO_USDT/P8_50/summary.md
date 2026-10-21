# EMA Hourly Continuation — IO/USDT P8_50

**Symbol:** IO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 608 |
| net_profit_factor | 0.7997 |
| net_win_rate | 0.4803 |
| gross_profit_factor | 0.9526 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -2.0749 |
| sortino_ratio | -0.7524 |
| max_drawdown | 0.5930 |
| cagr | -0.2940 |
| net_avg_win | 76.5365 |
| net_avg_loss | -88.4427 |
| avg_hold_time_bars | 14.8503 |
| exposure | 0.4371 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
