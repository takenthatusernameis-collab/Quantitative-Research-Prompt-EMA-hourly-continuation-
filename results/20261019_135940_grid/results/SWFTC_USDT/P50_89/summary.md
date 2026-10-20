# EMA Hourly Continuation — SWFTC/USDT P50_89

**Symbol:** SWFTC/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 671 |
| net_profit_factor | 0.4425 |
| net_win_rate | 0.4203 |
| gross_profit_factor | 0.8483 |
| gross_win_rate | 0.4411 |
| sharpe_ratio | -7.2599 |
| sortino_ratio | -2.6580 |
| max_drawdown | 0.9654 |
| cagr | -0.7381 |
| net_avg_win | 27.1775 |
| net_avg_loss | -44.5204 |
| avg_hold_time_bars | 4.4232 |
| exposure | 0.1349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
