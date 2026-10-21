# EMA Hourly Continuation — CGPT/USDT P50_144

**Symbol:** CGPT/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.8008 |
| net_win_rate | 0.4913 |
| gross_profit_factor | 0.9695 |
| gross_win_rate | 0.4913 |
| sharpe_ratio | -1.3294 |
| sortino_ratio | -0.3535 |
| max_drawdown | 0.3529 |
| cagr | -0.1510 |
| net_avg_win | 79.7175 |
| net_avg_loss | -96.1509 |
| avg_hold_time_bars | 17.3382 |
| exposure | 0.2727 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
