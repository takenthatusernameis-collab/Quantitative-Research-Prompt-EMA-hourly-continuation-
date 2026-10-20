# EMA Hourly Continuation — ORBS/USDT P34_100

**Symbol:** ORBS/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 729 |
| net_profit_factor | 0.5048 |
| net_win_rate | 0.4170 |
| gross_profit_factor | 0.8812 |
| gross_win_rate | 0.4348 |
| sharpe_ratio | -7.1067 |
| sortino_ratio | -2.7100 |
| max_drawdown | 0.9658 |
| cagr | -0.7347 |
| net_avg_win | 32.3360 |
| net_avg_loss | -45.8192 |
| avg_hold_time_bars | 8.7572 |
| exposure | 0.2902 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
