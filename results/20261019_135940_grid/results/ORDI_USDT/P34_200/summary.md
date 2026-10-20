# EMA Hourly Continuation — ORDI/USDT P34_200

**Symbol:** ORDI/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.7323 |
| net_win_rate | 0.4840 |
| gross_profit_factor | 0.9833 |
| gross_win_rate | 0.4886 |
| sharpe_ratio | -2.3168 |
| sortino_ratio | -0.6834 |
| max_drawdown | 0.5823 |
| cagr | -0.2765 |
| net_avg_win | 71.7944 |
| net_avg_loss | -91.9691 |
| avg_hold_time_bars | 23.4498 |
| exposure | 0.4669 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
