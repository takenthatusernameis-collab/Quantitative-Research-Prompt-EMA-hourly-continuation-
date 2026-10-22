# EMA Hourly Continuation — LUNA/USDT P34_200

**Symbol:** LUNA/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.6771 |
| net_win_rate | 0.4499 |
| gross_profit_factor | 0.8338 |
| gross_win_rate | 0.4499 |
| sharpe_ratio | -2.4025 |
| sortino_ratio | -0.6363 |
| max_drawdown | 0.5372 |
| cagr | -0.2547 |
| net_avg_win | 69.7372 |
| net_avg_loss | -84.2167 |
| avg_hold_time_bars | 28.6304 |
| exposure | 0.4542 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
