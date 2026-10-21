# EMA Hourly Continuation — DYDX/USDT P12_89

**Symbol:** DYDX/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.8337 |
| net_win_rate | 0.5013 |
| gross_profit_factor | 1.0061 |
| gross_win_rate | 0.5013 |
| sharpe_ratio | -1.1429 |
| sortino_ratio | -0.3208 |
| max_drawdown | 0.3604 |
| cagr | -0.1391 |
| net_avg_win | 81.4385 |
| net_avg_loss | -98.1902 |
| avg_hold_time_bars | 35.9948 |
| exposure | 0.6299 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
