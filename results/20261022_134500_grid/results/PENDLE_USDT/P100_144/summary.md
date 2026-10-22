# EMA Hourly Continuation — PENDLE/USDT P100_144

**Symbol:** PENDLE/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.4111 |
| net_win_rate | 0.4112 |
| gross_profit_factor | 0.7256 |
| gross_win_rate | 0.4280 |
| sharpe_ratio | -6.2575 |
| sortino_ratio | -2.0505 |
| max_drawdown | 0.9207 |
| cagr | -0.6343 |
| net_avg_win | 29.1960 |
| net_avg_loss | -49.5982 |
| avg_hold_time_bars | 3.5701 |
| exposure | 0.0868 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
