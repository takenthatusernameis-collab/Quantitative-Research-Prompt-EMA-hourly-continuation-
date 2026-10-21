# EMA Hourly Continuation — ORCA/USDT P12_100

**Symbol:** ORCA/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.8595 |
| net_win_rate | 0.5246 |
| gross_profit_factor | 1.0729 |
| gross_win_rate | 0.5246 |
| sharpe_ratio | -0.9042 |
| sortino_ratio | -0.2801 |
| max_drawdown | 0.3802 |
| cagr | -0.1250 |
| net_avg_win | 71.1127 |
| net_avg_loss | -91.3120 |
| avg_hold_time_bars | 28.2784 |
| exposure | 0.6003 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
