# EMA Hourly Continuation — VELO/USDT P21_200

**Symbol:** VELO/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.9802 |
| net_win_rate | 0.5303 |
| gross_profit_factor | 1.1137 |
| gross_win_rate | 0.5303 |
| sharpe_ratio | -0.0537 |
| sortino_ratio | -0.0141 |
| max_drawdown | 0.1870 |
| cagr | -0.0126 |
| net_avg_win | 89.1454 |
| net_avg_loss | -102.6762 |
| avg_hold_time_bars | 40.2636 |
| exposure | 0.6040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
