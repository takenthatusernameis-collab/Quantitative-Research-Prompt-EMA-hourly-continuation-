# EMA Hourly Continuation — BLUR/USDT P100_200

**Symbol:** BLUR/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 0.8508 |
| net_win_rate | 0.5226 |
| gross_profit_factor | 1.0854 |
| gross_win_rate | 0.5226 |
| sharpe_ratio | -0.7983 |
| sortino_ratio | -0.1870 |
| max_drawdown | 0.2518 |
| cagr | -0.0843 |
| net_avg_win | 81.7099 |
| net_avg_loss | -105.1106 |
| avg_hold_time_bars | 15.2218 |
| exposure | 0.1832 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
