# EMA Hourly Continuation — IO/USDT P20_26

**Symbol:** IO/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1123 |
| net_profit_factor | 0.3530 |
| net_win_rate | 0.3918 |
| gross_profit_factor | 0.7019 |
| gross_win_rate | 0.4150 |
| sharpe_ratio | -12.0982 |
| sortino_ratio | -5.9757 |
| max_drawdown | 0.9993 |
| cagr | -0.9551 |
| net_avg_win | 12.3892 |
| net_avg_loss | -22.6129 |
| avg_hold_time_bars | 1.9243 |
| exposure | 0.1046 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
