# EMA Hourly Continuation — GALA/USDT P8_144

**Symbol:** GALA/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 414 |
| net_profit_factor | 0.7211 |
| net_win_rate | 0.4952 |
| gross_profit_factor | 0.9844 |
| gross_win_rate | 0.4976 |
| sharpe_ratio | -2.0384 |
| sortino_ratio | -0.5844 |
| max_drawdown | 0.5141 |
| cagr | -0.2445 |
| net_avg_win | 63.7621 |
| net_avg_loss | -86.7257 |
| avg_hold_time_bars | 41.3551 |
| exposure | 0.7782 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
