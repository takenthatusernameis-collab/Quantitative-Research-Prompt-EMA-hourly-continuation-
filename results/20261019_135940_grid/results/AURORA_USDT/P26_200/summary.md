# EMA Hourly Continuation — AURORA/USDT P26_200

**Symbol:** AURORA/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.5690 |
| net_win_rate | 0.4450 |
| gross_profit_factor | 0.8323 |
| gross_win_rate | 0.4525 |
| sharpe_ratio | -3.6283 |
| sortino_ratio | -1.0192 |
| max_drawdown | 0.7161 |
| cagr | -0.3856 |
| net_avg_win | 52.3322 |
| net_avg_loss | -73.7497 |
| avg_hold_time_bars | 28.7375 |
| exposure | 0.5225 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
