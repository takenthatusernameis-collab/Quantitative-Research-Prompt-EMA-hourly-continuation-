# EMA Hourly Continuation — MANTA/USDT P26_200

**Symbol:** MANTA/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 318 |
| net_profit_factor | 0.7435 |
| net_win_rate | 0.4811 |
| gross_profit_factor | 0.9539 |
| gross_win_rate | 0.4811 |
| sharpe_ratio | -1.8341 |
| sortino_ratio | -0.4643 |
| max_drawdown | 0.4631 |
| cagr | -0.1938 |
| net_avg_win | 79.1705 |
| net_avg_loss | -98.7405 |
| avg_hold_time_bars | 44.2673 |
| exposure | 0.6399 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
