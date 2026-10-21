# EMA Hourly Continuation — AERO/USDT P21_55

**Symbol:** AERO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.8284 |
| net_win_rate | 0.5108 |
| gross_profit_factor | 1.0423 |
| gross_win_rate | 0.5108 |
| sharpe_ratio | -1.2787 |
| sortino_ratio | -0.3949 |
| max_drawdown | 0.4115 |
| cagr | -0.1674 |
| net_avg_win | 75.4167 |
| net_avg_loss | -95.0721 |
| avg_hold_time_bars | 8.2316 |
| exposure | 0.1729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
