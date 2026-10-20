# EMA Hourly Continuation — DYDX/USDT P8_144

**Symbol:** DYDX/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.7297 |
| net_win_rate | 0.5057 |
| gross_profit_factor | 1.0418 |
| gross_win_rate | 0.5080 |
| sharpe_ratio | -2.1394 |
| sortino_ratio | -0.6276 |
| max_drawdown | 0.5493 |
| cagr | -0.2610 |
| net_avg_win | 64.9969 |
| net_avg_loss | -91.1349 |
| avg_hold_time_bars | 38.7574 |
| exposure | 0.7699 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
