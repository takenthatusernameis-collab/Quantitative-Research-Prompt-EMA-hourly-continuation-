# EMA Hourly Continuation — ONDO/USDT P20_200

**Symbol:** ONDO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.7498 |
| net_win_rate | 0.5012 |
| gross_profit_factor | 1.0053 |
| gross_win_rate | 0.5012 |
| sharpe_ratio | -1.9115 |
| sortino_ratio | -0.5636 |
| max_drawdown | 0.5285 |
| cagr | -0.2335 |
| net_avg_win | 67.2772 |
| net_avg_loss | -90.1442 |
| avg_hold_time_bars | 28.7968 |
| exposure | 0.5668 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
