# EMA Hourly Continuation — CELR/USDT P12_200

**Symbol:** CELR/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.6551 |
| net_win_rate | 0.4595 |
| gross_profit_factor | 0.8769 |
| gross_win_rate | 0.4649 |
| sharpe_ratio | -2.6558 |
| sortino_ratio | -0.7185 |
| max_drawdown | 0.5765 |
| cagr | -0.2864 |
| net_avg_win | 64.0244 |
| net_avg_loss | -83.0781 |
| avg_hold_time_bars | 45.4405 |
| exposure | 0.7608 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
