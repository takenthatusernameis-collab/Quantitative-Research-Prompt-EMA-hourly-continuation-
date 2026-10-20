# EMA Hourly Continuation — ARKM/USDT P21_50

**Symbol:** ARKM/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1022 |
| net_profit_factor | 0.6002 |
| net_win_rate | 0.4501 |
| gross_profit_factor | 0.9617 |
| gross_win_rate | 0.4599 |
| sharpe_ratio | -6.7127 |
| sortino_ratio | -3.0271 |
| max_drawdown | 0.9758 |
| cagr | -0.7668 |
| net_avg_win | 31.7871 |
| net_avg_loss | -43.3519 |
| avg_hold_time_bars | 4.3689 |
| exposure | 0.2030 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
