# EMA Hourly Continuation — VELO/USDT P55_89

**Symbol:** VELO/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 296 |
| net_profit_factor | 0.7163 |
| net_win_rate | 0.4764 |
| gross_profit_factor | 0.8991 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -1.7733 |
| sortino_ratio | -0.4352 |
| max_drawdown | 0.4361 |
| cagr | -0.1812 |
| net_avg_win | 70.6738 |
| net_avg_loss | -89.7514 |
| avg_hold_time_bars | 7.0878 |
| exposure | 0.0954 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
