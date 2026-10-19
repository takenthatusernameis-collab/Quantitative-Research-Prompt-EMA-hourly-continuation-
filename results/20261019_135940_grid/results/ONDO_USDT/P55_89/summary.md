# EMA Hourly Continuation — ONDO/USDT P55_89

**Symbol:** ONDO/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.4431 |
| net_win_rate | 0.4098 |
| gross_profit_factor | 0.7669 |
| gross_win_rate | 0.4260 |
| sharpe_ratio | -7.0878 |
| sortino_ratio | -2.6091 |
| max_drawdown | 0.9598 |
| cagr | -0.7195 |
| net_avg_win | 27.5385 |
| net_avg_loss | -43.1512 |
| avg_hold_time_bars | 3.8905 |
| exposure | 0.1195 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
