# EMA Hourly Continuation — IO/USDT P8_50

**Symbol:** IO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1033 |
| net_profit_factor | 0.6310 |
| net_win_rate | 0.4569 |
| gross_profit_factor | 0.9050 |
| gross_win_rate | 0.4637 |
| sharpe_ratio | -5.6754 |
| sortino_ratio | -2.6439 |
| max_drawdown | 0.9510 |
| cagr | -0.7186 |
| net_avg_win | 34.4122 |
| net_avg_loss | -45.8814 |
| avg_hold_time_bars | 9.4366 |
| exposure | 0.4719 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
