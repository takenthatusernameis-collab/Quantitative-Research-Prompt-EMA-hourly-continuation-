# EMA Hourly Continuation — DASH/USDT P55_144

**Symbol:** DASH/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.7848 |
| net_win_rate | 0.5086 |
| gross_profit_factor | 1.0270 |
| gross_win_rate | 0.5086 |
| sharpe_ratio | -1.3433 |
| sortino_ratio | -0.3598 |
| max_drawdown | 0.4110 |
| cagr | -0.1531 |
| net_avg_win | 70.2700 |
| net_avg_loss | -92.6848 |
| avg_hold_time_bars | 12.4885 |
| exposure | 0.1975 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
