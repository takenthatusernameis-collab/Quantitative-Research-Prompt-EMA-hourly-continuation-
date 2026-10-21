# EMA Hourly Continuation — CELR/USDT P21_50

**Symbol:** CELR/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 593 |
| net_profit_factor | 0.7148 |
| net_win_rate | 0.4840 |
| gross_profit_factor | 0.9761 |
| gross_win_rate | 0.4840 |
| sharpe_ratio | -2.9370 |
| sortino_ratio | -1.0215 |
| max_drawdown | 0.7185 |
| cagr | -0.3738 |
| net_avg_win | 60.5013 |
| net_avg_loss | -79.3894 |
| avg_hold_time_bars | 7.7622 |
| exposure | 0.2083 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
