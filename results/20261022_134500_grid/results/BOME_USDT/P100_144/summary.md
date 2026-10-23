# EMA Hourly Continuation — BOME/USDT P100_144

**Symbol:** BOME/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.4844 |
| net_win_rate | 0.4620 |
| gross_profit_factor | 0.7768 |
| gross_win_rate | 0.4640 |
| sharpe_ratio | -4.3374 |
| sortino_ratio | -1.3743 |
| max_drawdown | 0.8105 |
| cagr | -0.4778 |
| net_avg_win | 32.7107 |
| net_avg_loss | -57.9942 |
| avg_hold_time_bars | 4.0640 |
| exposure | 0.0924 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
