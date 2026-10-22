# EMA Hourly Continuation — CARV/USDT P34_200

**Symbol:** CARV/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 245 |
| net_profit_factor | 0.6357 |
| net_win_rate | 0.4408 |
| gross_profit_factor | 0.7810 |
| gross_win_rate | 0.4408 |
| sharpe_ratio | -2.3765 |
| sortino_ratio | -0.5855 |
| max_drawdown | 0.4502 |
| cagr | -0.2358 |
| net_avg_win | 67.9525 |
| net_avg_loss | -84.2624 |
| avg_hold_time_bars | 32.4286 |
| exposure | 0.4471 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
