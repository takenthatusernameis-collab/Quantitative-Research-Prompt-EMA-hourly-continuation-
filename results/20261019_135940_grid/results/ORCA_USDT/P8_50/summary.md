# EMA Hourly Continuation — ORCA/USDT P8_50

**Symbol:** ORCA/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1047 |
| net_profit_factor | 0.6575 |
| net_win_rate | 0.4900 |
| gross_profit_factor | 0.9926 |
| gross_win_rate | 0.4976 |
| sharpe_ratio | -4.6386 |
| sortino_ratio | -2.1103 |
| max_drawdown | 0.9271 |
| cagr | -0.6379 |
| net_avg_win | 34.4993 |
| net_avg_loss | -50.4087 |
| avg_hold_time_bars | 9.4862 |
| exposure | 0.4515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
