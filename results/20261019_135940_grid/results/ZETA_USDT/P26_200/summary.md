# EMA Hourly Continuation — ZETA/USDT P26_200

**Symbol:** ZETA/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.8005 |
| net_win_rate | 0.5089 |
| gross_profit_factor | 1.0740 |
| gross_win_rate | 0.5119 |
| sharpe_ratio | -1.4034 |
| sortino_ratio | -0.3635 |
| max_drawdown | 0.4430 |
| cagr | -0.1593 |
| net_avg_win | 83.1765 |
| net_avg_loss | -107.6854 |
| avg_hold_time_bars | 40.6429 |
| exposure | 0.6179 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
