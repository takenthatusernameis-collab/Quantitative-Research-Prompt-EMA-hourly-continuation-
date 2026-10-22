# EMA Hourly Continuation — AGLD/USDT P34_50

**Symbol:** AGLD/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.6163 |
| net_win_rate | 0.4636 |
| gross_profit_factor | 0.9009 |
| gross_win_rate | 0.4636 |
| sharpe_ratio | -3.4683 |
| sortino_ratio | -1.0396 |
| max_drawdown | 0.7241 |
| cagr | -0.3784 |
| net_avg_win | 54.9937 |
| net_avg_loss | -77.1385 |
| avg_hold_time_bars | 5.3409 |
| exposure | 0.1063 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
