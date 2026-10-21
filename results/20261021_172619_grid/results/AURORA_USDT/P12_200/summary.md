# EMA Hourly Continuation — AURORA/USDT P12_200

**Symbol:** AURORA/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 359 |
| net_profit_factor | 0.6815 |
| net_win_rate | 0.4568 |
| gross_profit_factor | 0.8530 |
| gross_win_rate | 0.4568 |
| sharpe_ratio | -2.4132 |
| sortino_ratio | -0.6484 |
| max_drawdown | 0.5427 |
| cagr | -0.2594 |
| net_avg_win | 69.0924 |
| net_avg_loss | -85.2627 |
| avg_hold_time_bars | 39.0251 |
| exposure | 0.6368 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
