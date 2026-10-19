# EMA Hourly Continuation — AERO/USDT P89_100

**Symbol:** AERO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.2569 |
| net_win_rate | 0.3917 |
| gross_profit_factor | 0.6441 |
| gross_win_rate | 0.4154 |
| sharpe_ratio | -8.0843 |
| sortino_ratio | -2.6225 |
| max_drawdown | 0.9673 |
| cagr | -0.7430 |
| net_avg_win | 16.8028 |
| net_avg_loss | -42.1164 |
| avg_hold_time_bars | 2.1122 |
| exposure | 0.0488 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
