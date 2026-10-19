# EMA Hourly Continuation — PENDLE/USDT P55_144

**Symbol:** PENDLE/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.6348 |
| net_win_rate | 0.4774 |
| gross_profit_factor | 0.8982 |
| gross_win_rate | 0.4794 |
| sharpe_ratio | -3.1248 |
| sortino_ratio | -0.9918 |
| max_drawdown | 0.7050 |
| cagr | -0.3768 |
| net_avg_win | 49.7154 |
| net_avg_loss | -71.5479 |
| avg_hold_time_bars | 11.4381 |
| exposure | 0.2646 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
