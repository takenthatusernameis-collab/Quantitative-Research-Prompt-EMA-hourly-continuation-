# EMA Hourly Continuation — ZBCN/USDT P100_144

**Symbol:** ZBCN/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 197 |
| net_profit_factor | 0.8993 |
| net_win_rate | 0.5279 |
| gross_profit_factor | 1.1056 |
| gross_win_rate | 0.5279 |
| sharpe_ratio | -0.4234 |
| sortino_ratio | -0.0865 |
| max_drawdown | 0.1779 |
| cagr | -0.0410 |
| net_avg_win | 84.3067 |
| net_avg_loss | -104.8328 |
| avg_hold_time_bars | 6.5939 |
| exposure | 0.0601 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
