# EMA Hourly Continuation — CELR/USDT P12_34

**Symbol:** CELR/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 734 |
| net_profit_factor | 0.6396 |
| net_win_rate | 0.4591 |
| gross_profit_factor | 0.8685 |
| gross_win_rate | 0.4591 |
| sharpe_ratio | -4.0477 |
| sortino_ratio | -1.5603 |
| max_drawdown | 0.8389 |
| cagr | -0.5110 |
| net_avg_win | 43.9924 |
| net_avg_loss | -58.3873 |
| avg_hold_time_bars | 6.9550 |
| exposure | 0.2310 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
