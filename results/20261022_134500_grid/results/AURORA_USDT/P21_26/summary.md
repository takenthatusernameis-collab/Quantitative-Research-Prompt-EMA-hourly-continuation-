# EMA Hourly Continuation — AURORA/USDT P21_26

**Symbol:** AURORA/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1009 |
| net_profit_factor | 0.1488 |
| net_win_rate | 0.2854 |
| gross_profit_factor | 0.5496 |
| gross_win_rate | 0.3508 |
| sharpe_ratio | -16.1412 |
| sortino_ratio | -7.7433 |
| max_drawdown | 1.0000 |
| cagr | -0.9861 |
| net_avg_win | 6.0713 |
| net_avg_loss | -16.2945 |
| avg_hold_time_bars | 2.7116 |
| exposure | 0.1244 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
