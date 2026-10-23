# EMA Hourly Continuation — ANYONE/USDT P26_200

**Symbol:** ANYONE/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 284 |
| net_profit_factor | 0.6809 |
| net_win_rate | 0.4542 |
| gross_profit_factor | 0.8226 |
| gross_win_rate | 0.4542 |
| sharpe_ratio | -2.1482 |
| sortino_ratio | -0.5353 |
| max_drawdown | 0.4755 |
| cagr | -0.2233 |
| net_avg_win | 71.9343 |
| net_avg_loss | -87.9254 |
| avg_hold_time_bars | 43.4472 |
| exposure | 0.6235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
