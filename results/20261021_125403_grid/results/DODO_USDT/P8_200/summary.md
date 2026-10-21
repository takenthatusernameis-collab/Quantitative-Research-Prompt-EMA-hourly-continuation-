# EMA Hourly Continuation — DODO/USDT P8_200

**Symbol:** DODO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.6793 |
| net_win_rate | 0.4406 |
| gross_profit_factor | 0.8096 |
| gross_win_rate | 0.4406 |
| sharpe_ratio | -2.6048 |
| sortino_ratio | -0.7382 |
| max_drawdown | 0.5983 |
| cagr | -0.2885 |
| net_avg_win | 68.5569 |
| net_avg_loss | -79.4916 |
| avg_hold_time_bars | 39.4604 |
| exposure | 0.7214 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
