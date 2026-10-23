# EMA Hourly Continuation — CARV/USDT P26_144

**Symbol:** CARV/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.5621 |
| net_win_rate | 0.4474 |
| gross_profit_factor | 0.8536 |
| gross_win_rate | 0.4572 |
| sharpe_ratio | -4.1257 |
| sortino_ratio | -1.3101 |
| max_drawdown | 0.7365 |
| cagr | -0.4604 |
| net_avg_win | 50.0786 |
| net_avg_loss | -72.1406 |
| avg_hold_time_bars | 19.6919 |
| exposure | 0.4532 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
