# EMA Hourly Continuation — SWFTC/USDT P100_144

**Symbol:** SWFTC/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 183 |
| net_profit_factor | 0.7445 |
| net_win_rate | 0.4973 |
| gross_profit_factor | 0.9881 |
| gross_win_rate | 0.4973 |
| sharpe_ratio | -1.2485 |
| sortino_ratio | -0.2421 |
| max_drawdown | 0.2651 |
| cagr | -0.1051 |
| net_avg_win | 77.9337 |
| net_avg_loss | -103.5381 |
| avg_hold_time_bars | 7.1202 |
| exposure | 0.0592 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
