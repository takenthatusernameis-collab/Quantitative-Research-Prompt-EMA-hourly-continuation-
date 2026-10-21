# EMA Hourly Continuation — BOME/USDT P34_89

**Symbol:** BOME/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.8526 |
| net_win_rate | 0.5184 |
| gross_profit_factor | 1.0487 |
| gross_win_rate | 0.5184 |
| sharpe_ratio | -0.9137 |
| sortino_ratio | -0.2830 |
| max_drawdown | 0.3405 |
| cagr | -0.1247 |
| net_avg_win | 68.5295 |
| net_avg_loss | -86.5064 |
| avg_hold_time_bars | 9.7473 |
| exposure | 0.2051 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
