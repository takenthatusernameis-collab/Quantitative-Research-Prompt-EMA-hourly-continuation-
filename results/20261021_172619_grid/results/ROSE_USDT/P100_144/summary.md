# EMA Hourly Continuation — ROSE/USDT P100_144

**Symbol:** ROSE/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 232 |
| net_profit_factor | 0.8553 |
| net_win_rate | 0.5345 |
| gross_profit_factor | 1.1332 |
| gross_win_rate | 0.5345 |
| sharpe_ratio | -0.6894 |
| sortino_ratio | -0.1519 |
| max_drawdown | 0.2148 |
| cagr | -0.0686 |
| net_avg_win | 77.9124 |
| net_avg_loss | -104.5879 |
| avg_hold_time_bars | 6.6379 |
| exposure | 0.0700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
