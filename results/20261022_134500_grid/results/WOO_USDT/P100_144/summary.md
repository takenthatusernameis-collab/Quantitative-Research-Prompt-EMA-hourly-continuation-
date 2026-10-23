# EMA Hourly Continuation — WOO/USDT P100_144

**Symbol:** WOO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.4733 |
| net_win_rate | 0.4372 |
| gross_profit_factor | 0.8329 |
| gross_win_rate | 0.4498 |
| sharpe_ratio | -5.1245 |
| sortino_ratio | -1.5944 |
| max_drawdown | 0.8521 |
| cagr | -0.5328 |
| net_avg_win | 36.6357 |
| net_avg_loss | -60.1390 |
| avg_hold_time_bars | 3.9079 |
| exposure | 0.0849 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
