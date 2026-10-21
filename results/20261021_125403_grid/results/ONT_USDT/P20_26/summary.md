# EMA Hourly Continuation — ONT/USDT P20_26

**Symbol:** ONT/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 232 |
| net_profit_factor | 0.6778 |
| net_win_rate | 0.5043 |
| gross_profit_factor | 1.0032 |
| gross_win_rate | 0.5043 |
| sharpe_ratio | -1.7880 |
| sortino_ratio | -0.3912 |
| max_drawdown | 0.4081 |
| cagr | -0.1637 |
| net_avg_win | 65.2747 |
| net_avg_loss | -97.9799 |
| avg_hold_time_bars | 5.5517 |
| exposure | 0.0583 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
