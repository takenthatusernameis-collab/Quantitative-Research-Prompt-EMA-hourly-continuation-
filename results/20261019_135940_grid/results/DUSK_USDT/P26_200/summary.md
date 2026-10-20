# EMA Hourly Continuation — DUSK/USDT P26_200

**Symbol:** DUSK/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.7497 |
| net_win_rate | 0.4870 |
| gross_profit_factor | 0.9658 |
| gross_win_rate | 0.4899 |
| sharpe_ratio | -1.6831 |
| sortino_ratio | -0.4431 |
| max_drawdown | 0.4523 |
| cagr | -0.1888 |
| net_avg_win | 72.4218 |
| net_avg_loss | -91.7209 |
| avg_hold_time_bars | 36.9856 |
| exposure | 0.5834 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
