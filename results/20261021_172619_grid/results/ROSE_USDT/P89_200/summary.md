# EMA Hourly Continuation — ROSE/USDT P89_200

**Symbol:** ROSE/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 277 |
| net_profit_factor | 0.8988 |
| net_win_rate | 0.5271 |
| gross_profit_factor | 1.0960 |
| gross_win_rate | 0.5271 |
| sharpe_ratio | -0.4746 |
| sortino_ratio | -0.1139 |
| max_drawdown | 0.1878 |
| cagr | -0.0540 |
| net_avg_win | 79.1629 |
| net_avg_loss | -98.1562 |
| avg_hold_time_bars | 15.1408 |
| exposure | 0.1906 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
