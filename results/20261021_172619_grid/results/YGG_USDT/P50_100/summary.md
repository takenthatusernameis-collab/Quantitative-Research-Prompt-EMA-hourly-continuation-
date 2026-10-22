# EMA Hourly Continuation — YGG/USDT P50_100

**Symbol:** YGG/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.7891 |
| net_win_rate | 0.5091 |
| gross_profit_factor | 1.0209 |
| gross_win_rate | 0.5091 |
| sharpe_ratio | -1.4979 |
| sortino_ratio | -0.4503 |
| max_drawdown | 0.4387 |
| cagr | -0.1875 |
| net_avg_win | 68.0801 |
| net_avg_loss | -89.4738 |
| avg_hold_time_bars | 7.8068 |
| exposure | 0.1554 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
