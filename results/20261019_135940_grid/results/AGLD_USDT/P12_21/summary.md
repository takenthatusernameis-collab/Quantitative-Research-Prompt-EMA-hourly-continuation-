# EMA Hourly Continuation — AGLD/USDT P12_21

**Symbol:** AGLD/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1361 |
| net_profit_factor | 0.3642 |
| net_win_rate | 0.4151 |
| gross_profit_factor | 0.8617 |
| gross_win_rate | 0.4497 |
| sharpe_ratio | -10.9893 |
| sortino_ratio | -5.7500 |
| max_drawdown | 0.9992 |
| cagr | -0.9417 |
| net_avg_win | 10.1292 |
| net_avg_loss | -19.7428 |
| avg_hold_time_bars | 3.2946 |
| exposure | 0.2029 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
