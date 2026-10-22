# EMA Hourly Continuation — BONK/USDT P34_55

**Symbol:** BONK/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 869 |
| net_profit_factor | 0.4939 |
| net_win_rate | 0.4557 |
| gross_profit_factor | 0.8867 |
| gross_win_rate | 0.4695 |
| sharpe_ratio | -6.8860 |
| sortino_ratio | -2.8518 |
| max_drawdown | 0.9728 |
| cagr | -0.7586 |
| net_avg_win | 23.9455 |
| net_avg_loss | -40.5933 |
| avg_hold_time_bars | 2.8320 |
| exposure | 0.1119 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
