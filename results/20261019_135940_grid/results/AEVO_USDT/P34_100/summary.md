# EMA Hourly Continuation — AEVO/USDT P34_100

**Symbol:** AEVO/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 662 |
| net_profit_factor | 0.6650 |
| net_win_rate | 0.4924 |
| gross_profit_factor | 0.9804 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -3.3591 |
| sortino_ratio | -1.2206 |
| max_drawdown | 0.7792 |
| cagr | -0.4383 |
| net_avg_win | 46.6843 |
| net_avg_loss | -68.1102 |
| avg_hold_time_bars | 10.2855 |
| exposure | 0.3081 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
