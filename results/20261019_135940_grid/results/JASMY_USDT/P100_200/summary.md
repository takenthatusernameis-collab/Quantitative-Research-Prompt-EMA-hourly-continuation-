# EMA Hourly Continuation — JASMY/USDT P100_200

**Symbol:** JASMY/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.7171 |
| net_win_rate | 0.5342 |
| gross_profit_factor | 1.0971 |
| gross_win_rate | 0.5342 |
| sharpe_ratio | -1.7818 |
| sortino_ratio | -0.4896 |
| max_drawdown | 0.4525 |
| cagr | -0.2105 |
| net_avg_win | 55.8997 |
| net_avg_loss | -89.3973 |
| avg_hold_time_bars | 11.0368 |
| exposure | 0.1906 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
