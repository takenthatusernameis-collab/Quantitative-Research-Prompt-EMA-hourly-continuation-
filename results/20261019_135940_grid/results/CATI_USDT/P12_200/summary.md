# EMA Hourly Continuation — CATI/USDT P12_200

**Symbol:** CATI/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.4960 |
| net_win_rate | 0.4164 |
| gross_profit_factor | 0.7621 |
| gross_win_rate | 0.4361 |
| sharpe_ratio | -4.3392 |
| sortino_ratio | -1.1608 |
| max_drawdown | 0.7251 |
| cagr | -0.4343 |
| net_avg_win | 53.8304 |
| net_avg_loss | -77.4327 |
| avg_hold_time_bars | 46.1279 |
| exposure | 0.7712 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
