# EMA Hourly Continuation — CETUS/USDT P50_144

**Symbol:** CETUS/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.9596 |
| net_win_rate | 0.5405 |
| gross_profit_factor | 1.1659 |
| gross_win_rate | 0.5405 |
| sharpe_ratio | -0.1885 |
| sortino_ratio | -0.0506 |
| max_drawdown | 0.1756 |
| cagr | -0.0286 |
| net_avg_win | 89.5939 |
| net_avg_loss | -109.8100 |
| avg_hold_time_bars | 18.5202 |
| exposure | 0.2900 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
