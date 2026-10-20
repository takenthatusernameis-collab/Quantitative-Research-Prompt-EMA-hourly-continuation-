# EMA Hourly Continuation — FIDA/USDT P144_200

**Symbol:** FIDA/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.4235 |
| net_win_rate | 0.4237 |
| gross_profit_factor | 0.7474 |
| gross_win_rate | 0.4396 |
| sharpe_ratio | -5.1888 |
| sortino_ratio | -1.5414 |
| max_drawdown | 0.8469 |
| cagr | -0.5221 |
| net_avg_win | 33.3688 |
| net_avg_loss | -57.9203 |
| avg_hold_time_bars | 5.2323 |
| exposure | 0.1039 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
