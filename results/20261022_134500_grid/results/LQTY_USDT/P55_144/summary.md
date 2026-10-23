# EMA Hourly Continuation — LQTY/USDT P55_144

**Symbol:** LQTY/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.5689 |
| net_win_rate | 0.4533 |
| gross_profit_factor | 0.8474 |
| gross_win_rate | 0.4629 |
| sharpe_ratio | -3.9906 |
| sortino_ratio | -1.2887 |
| max_drawdown | 0.7860 |
| cagr | -0.4553 |
| net_avg_win | 43.4654 |
| net_avg_loss | -63.3617 |
| avg_hold_time_bars | 10.9257 |
| exposure | 0.2596 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
