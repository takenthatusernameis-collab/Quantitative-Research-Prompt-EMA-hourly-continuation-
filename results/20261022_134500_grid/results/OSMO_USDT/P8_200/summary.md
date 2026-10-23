# EMA Hourly Continuation — OSMO/USDT P8_200

**Symbol:** OSMO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.7512 |
| net_win_rate | 0.4859 |
| gross_profit_factor | 1.0070 |
| gross_win_rate | 0.4936 |
| sharpe_ratio | -2.0098 |
| sortino_ratio | -0.5639 |
| max_drawdown | 0.5498 |
| cagr | -0.2317 |
| net_avg_win | 76.9213 |
| net_avg_loss | -96.7955 |
| avg_hold_time_bars | 44.1355 |
| exposure | 0.7844 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
