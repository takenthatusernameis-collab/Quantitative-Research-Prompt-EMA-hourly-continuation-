# EMA Hourly Continuation — CELR/USDT P8_12

**Symbol:** CELR/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.5679 |
| net_win_rate | 0.4475 |
| gross_profit_factor | 0.8499 |
| gross_win_rate | 0.4475 |
| sharpe_ratio | -4.2083 |
| sortino_ratio | -1.3113 |
| max_drawdown | 0.7918 |
| cagr | -0.4525 |
| net_avg_win | 48.2042 |
| net_avg_loss | -68.7449 |
| avg_hold_time_bars | 4.2500 |
| exposure | 0.0915 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
