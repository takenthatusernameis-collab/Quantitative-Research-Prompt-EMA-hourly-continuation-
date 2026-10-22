# EMA Hourly Continuation — WLD/USDT P21_34

**Symbol:** WLD/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1131 |
| net_profit_factor | 0.4367 |
| net_win_rate | 0.4562 |
| gross_profit_factor | 0.8468 |
| gross_win_rate | 0.4651 |
| sharpe_ratio | -8.4552 |
| sortino_ratio | -3.9954 |
| max_drawdown | 0.9938 |
| cagr | -0.8670 |
| net_avg_win | 14.9271 |
| net_avg_loss | -28.6818 |
| avg_hold_time_bars | 2.3519 |
| exposure | 0.1209 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
