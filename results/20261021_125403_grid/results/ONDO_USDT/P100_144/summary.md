# EMA Hourly Continuation — ONDO/USDT P100_144

**Symbol:** ONDO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 212 |
| net_profit_factor | 0.7982 |
| net_win_rate | 0.5094 |
| gross_profit_factor | 1.0329 |
| gross_win_rate | 0.5094 |
| sharpe_ratio | -1.0108 |
| sortino_ratio | -0.2116 |
| max_drawdown | 0.2687 |
| cagr | -0.0929 |
| net_avg_win | 79.5499 |
| net_avg_loss | -103.4899 |
| avg_hold_time_bars | 6.2170 |
| exposure | 0.0599 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
