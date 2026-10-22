# EMA Hourly Continuation — OSMO/USDT P34_89

**Symbol:** OSMO/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.6664 |
| net_win_rate | 0.4623 |
| gross_profit_factor | 0.8936 |
| gross_win_rate | 0.4623 |
| sharpe_ratio | -3.0289 |
| sortino_ratio | -0.9435 |
| max_drawdown | 0.6680 |
| cagr | -0.3514 |
| net_avg_win | 59.9297 |
| net_avg_loss | -77.3294 |
| avg_hold_time_bars | 10.7427 |
| exposure | 0.2334 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
