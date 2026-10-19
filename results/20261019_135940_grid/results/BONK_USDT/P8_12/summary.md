# EMA Hourly Continuation — BONK/USDT P8_12

**Symbol:** BONK/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1830 |
| net_profit_factor | 0.3047 |
| net_win_rate | 0.3678 |
| gross_profit_factor | 0.7235 |
| gross_win_rate | 0.3973 |
| sharpe_ratio | -17.0952 |
| sortino_ratio | -10.4771 |
| max_drawdown | 1.0000 |
| cagr | -0.9962 |
| net_avg_win | 6.5104 |
| net_avg_loss | -12.4300 |
| avg_hold_time_bars | 1.6448 |
| exposure | 0.1368 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
