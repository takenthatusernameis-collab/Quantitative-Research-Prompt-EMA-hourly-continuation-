# EMA Hourly Continuation — ORDI/USDT P21_26

**Symbol:** ORDI/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1178 |
| net_profit_factor | 0.2795 |
| net_win_rate | 0.3591 |
| gross_profit_factor | 0.8147 |
| gross_win_rate | 0.4024 |
| sharpe_ratio | -13.7878 |
| sortino_ratio | -6.8359 |
| max_drawdown | 0.9999 |
| cagr | -0.9734 |
| net_avg_win | 9.1680 |
| net_avg_loss | -18.3801 |
| avg_hold_time_bars | 1.9134 |
| exposure | 0.1025 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
