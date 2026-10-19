# EMA Hourly Continuation — AERO/USDT P34_144

**Symbol:** AERO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.7036 |
| net_win_rate | 0.4988 |
| gross_profit_factor | 1.0010 |
| gross_win_rate | 0.4988 |
| sharpe_ratio | -2.3765 |
| sortino_ratio | -0.6879 |
| max_drawdown | 0.5747 |
| cagr | -0.2868 |
| net_avg_win | 63.1540 |
| net_avg_loss | -89.3443 |
| avg_hold_time_bars | 19.0116 |
| exposure | 0.3725 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
