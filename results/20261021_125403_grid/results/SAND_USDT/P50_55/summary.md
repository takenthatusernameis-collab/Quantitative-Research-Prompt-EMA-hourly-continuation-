# EMA Hourly Continuation — SAND/USDT P50_55

**Symbol:** SAND/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 108 |
| net_profit_factor | 0.6552 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9893 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.3106 |
| sortino_ratio | -0.1963 |
| max_drawdown | 0.2093 |
| cagr | -0.0850 |
| net_avg_win | 70.3406 |
| net_avg_loss | -107.3606 |
| avg_hold_time_bars | 4.4907 |
| exposure | 0.0220 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
