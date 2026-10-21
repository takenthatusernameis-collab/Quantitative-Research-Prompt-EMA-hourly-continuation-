# EMA Hourly Continuation — DYDX/USDT P100_144

**Symbol:** DYDX/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 248 |
| net_profit_factor | 0.8286 |
| net_win_rate | 0.5282 |
| gross_profit_factor | 1.1197 |
| gross_win_rate | 0.5282 |
| sharpe_ratio | -0.9293 |
| sortino_ratio | -0.2113 |
| max_drawdown | 0.2653 |
| cagr | -0.0933 |
| net_avg_win | 80.4450 |
| net_avg_loss | -108.7007 |
| avg_hold_time_bars | 6.2460 |
| exposure | 0.0704 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
