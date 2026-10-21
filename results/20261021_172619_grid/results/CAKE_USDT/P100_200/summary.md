# EMA Hourly Continuation — CAKE/USDT P100_200

**Symbol:** CAKE/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 228 |
| net_profit_factor | 0.6750 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9184 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -1.7362 |
| sortino_ratio | -0.3744 |
| max_drawdown | 0.3837 |
| cagr | -0.1574 |
| net_avg_win | 65.4236 |
| net_avg_loss | -91.9521 |
| avg_hold_time_bars | 11.8860 |
| exposure | 0.1232 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
