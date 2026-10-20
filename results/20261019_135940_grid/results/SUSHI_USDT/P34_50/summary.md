# EMA Hourly Continuation — SUSHI/USDT P34_50

**Symbol:** SUSHI/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 955 |
| net_profit_factor | 0.3884 |
| net_win_rate | 0.4042 |
| gross_profit_factor | 0.8068 |
| gross_win_rate | 0.4325 |
| sharpe_ratio | -9.7919 |
| sortino_ratio | -4.2901 |
| max_drawdown | 0.9958 |
| cagr | -0.8857 |
| net_avg_win | 16.3814 |
| net_avg_loss | -28.6136 |
| avg_hold_time_bars | 2.7969 |
| exposure | 0.1209 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
