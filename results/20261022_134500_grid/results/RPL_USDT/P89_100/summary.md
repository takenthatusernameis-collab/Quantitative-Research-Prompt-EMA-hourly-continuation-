# EMA Hourly Continuation — RPL/USDT P89_100

**Symbol:** RPL/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.3733 |
| net_win_rate | 0.4202 |
| gross_profit_factor | 0.8833 |
| gross_win_rate | 0.4582 |
| sharpe_ratio | -6.9570 |
| sortino_ratio | -2.2954 |
| max_drawdown | 0.9402 |
| cagr | -0.6727 |
| net_avg_win | 25.3393 |
| net_avg_loss | -49.1873 |
| avg_hold_time_bars | 3.4829 |
| exposure | 0.0829 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
