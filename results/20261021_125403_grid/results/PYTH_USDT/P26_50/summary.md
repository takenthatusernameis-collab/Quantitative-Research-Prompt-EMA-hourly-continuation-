# EMA Hourly Continuation — PYTH/USDT P26_50

**Symbol:** PYTH/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.7023 |
| net_win_rate | 0.4728 |
| gross_profit_factor | 0.9119 |
| gross_win_rate | 0.4728 |
| sharpe_ratio | -2.3565 |
| sortino_ratio | -0.6760 |
| max_drawdown | 0.5529 |
| cagr | -0.2667 |
| net_avg_win | 66.8460 |
| net_avg_loss | -85.3480 |
| avg_hold_time_bars | 5.8960 |
| exposure | 0.1083 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
