# EMA Hourly Continuation — ETC/USDT P26_50

**Symbol:** ETC/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 979 |
| net_profit_factor | 0.3652 |
| net_win_rate | 0.4178 |
| gross_profit_factor | 0.9063 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -10.2823 |
| sortino_ratio | -4.5736 |
| max_drawdown | 0.9972 |
| cagr | -0.9032 |
| net_avg_win | 14.0274 |
| net_avg_loss | -27.5593 |
| avg_hold_time_bars | 3.4229 |
| exposure | 0.1523 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
