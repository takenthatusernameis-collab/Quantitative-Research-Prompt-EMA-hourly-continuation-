# EMA Hourly Continuation — PHA/USDT P8_20

**Symbol:** PHA/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 584 |
| net_profit_factor | 0.7719 |
| net_win_rate | 0.5017 |
| gross_profit_factor | 1.0190 |
| gross_win_rate | 0.5017 |
| sharpe_ratio | -2.0716 |
| sortino_ratio | -0.7185 |
| max_drawdown | 0.5853 |
| cagr | -0.2810 |
| net_avg_win | 65.0535 |
| net_avg_loss | -84.8568 |
| avg_hold_time_bars | 5.6695 |
| exposure | 0.1505 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
