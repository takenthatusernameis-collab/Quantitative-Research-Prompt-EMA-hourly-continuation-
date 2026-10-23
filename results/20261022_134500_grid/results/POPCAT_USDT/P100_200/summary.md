# EMA Hourly Continuation — POPCAT/USDT P100_200

**Symbol:** POPCAT/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.7231 |
| net_win_rate | 0.4941 |
| gross_profit_factor | 1.0035 |
| gross_win_rate | 0.5059 |
| sharpe_ratio | -2.0387 |
| sortino_ratio | -0.5754 |
| max_drawdown | 0.4612 |
| cagr | -0.2345 |
| net_avg_win | 68.5967 |
| net_avg_loss | -92.6489 |
| avg_hold_time_bars | 10.4556 |
| exposure | 0.1867 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
