# EMA Hourly Continuation — OSMO/USDT P8_20

**Symbol:** OSMO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 679 |
| net_profit_factor | 0.7642 |
| net_win_rate | 0.4993 |
| gross_profit_factor | 1.1439 |
| gross_win_rate | 0.4993 |
| sharpe_ratio | -3.3122 |
| sortino_ratio | -1.2414 |
| max_drawdown | 0.8294 |
| cagr | -0.4323 |
| net_avg_win | 72.5324 |
| net_avg_loss | -94.6354 |
| avg_hold_time_bars | 5.6907 |
| exposure | 0.1756 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
