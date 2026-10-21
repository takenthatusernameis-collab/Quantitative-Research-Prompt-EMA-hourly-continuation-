# EMA Hourly Continuation — DYDX/USDT P26_34

**Symbol:** DYDX/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 200 |
| net_profit_factor | 0.7215 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0087 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.4670 |
| sortino_ratio | -0.2982 |
| max_drawdown | 0.2882 |
| cagr | -0.1266 |
| net_avg_win | 74.6749 |
| net_avg_loss | -103.4933 |
| avg_hold_time_bars | 5.0850 |
| exposure | 0.0462 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
