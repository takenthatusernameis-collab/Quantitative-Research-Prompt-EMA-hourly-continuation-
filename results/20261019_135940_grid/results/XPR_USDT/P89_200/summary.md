# EMA Hourly Continuation — XPR/USDT P89_200

**Symbol:** XPR/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.4536 |
| net_win_rate | 0.4738 |
| gross_profit_factor | 0.8207 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -3.9929 |
| sortino_ratio | -1.1162 |
| max_drawdown | 0.7745 |
| cagr | -0.4295 |
| net_avg_win | 33.0267 |
| net_avg_loss | -65.5578 |
| avg_hold_time_bars | 10.1047 |
| exposure | 0.1842 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
