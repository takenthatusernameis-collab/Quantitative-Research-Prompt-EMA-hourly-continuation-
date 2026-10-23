# EMA Hourly Continuation — CELR/USDT P20_200

**Symbol:** CELR/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.5949 |
| net_win_rate | 0.4435 |
| gross_profit_factor | 0.8062 |
| gross_win_rate | 0.4463 |
| sharpe_ratio | -3.0782 |
| sortino_ratio | -0.8228 |
| max_drawdown | 0.6316 |
| cagr | -0.3221 |
| net_avg_win | 57.0157 |
| net_avg_loss | -76.3834 |
| avg_hold_time_bars | 41.2397 |
| exposure | 0.6774 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
