# EMA Hourly Continuation — CAKE/USDT P100_144

**Symbol:** CAKE/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 184 |
| net_profit_factor | 0.6980 |
| net_win_rate | 0.5109 |
| gross_profit_factor | 1.0280 |
| gross_win_rate | 0.5109 |
| sharpe_ratio | -1.4515 |
| sortino_ratio | -0.2836 |
| max_drawdown | 0.3089 |
| cagr | -0.1215 |
| net_avg_win | 68.3001 |
| net_avg_loss | -102.1970 |
| avg_hold_time_bars | 5.8967 |
| exposure | 0.0493 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
