# EMA Hourly Continuation — SWFTC/USDT P12_200

**Symbol:** SWFTC/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.6063 |
| net_win_rate | 0.4444 |
| gross_profit_factor | 0.8663 |
| gross_win_rate | 0.4481 |
| sharpe_ratio | -4.3463 |
| sortino_ratio | -1.4297 |
| max_drawdown | 0.8280 |
| cagr | -0.4966 |
| net_avg_win | 51.8494 |
| net_avg_loss | -68.4167 |
| avg_hold_time_bars | 25.1858 |
| exposure | 0.6285 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
