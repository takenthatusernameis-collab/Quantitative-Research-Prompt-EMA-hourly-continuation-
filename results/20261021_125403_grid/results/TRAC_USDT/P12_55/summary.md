# EMA Hourly Continuation — TRAC/USDT P12_55

**Symbol:** TRAC/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 569 |
| net_profit_factor | 0.7307 |
| net_win_rate | 0.4728 |
| gross_profit_factor | 0.9172 |
| gross_win_rate | 0.4728 |
| sharpe_ratio | -2.5140 |
| sortino_ratio | -0.8541 |
| max_drawdown | 0.6508 |
| cagr | -0.3246 |
| net_avg_win | 63.2270 |
| net_avg_loss | -77.5861 |
| avg_hold_time_bars | 12.9367 |
| exposure | 0.3346 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
