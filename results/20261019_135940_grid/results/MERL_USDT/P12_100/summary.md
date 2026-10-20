# EMA Hourly Continuation — MERL/USDT P12_100

**Symbol:** MERL/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 601 |
| net_profit_factor | 0.7508 |
| net_win_rate | 0.4842 |
| gross_profit_factor | 0.9829 |
| gross_win_rate | 0.4842 |
| sharpe_ratio | -2.5705 |
| sortino_ratio | -0.8878 |
| max_drawdown | 0.7001 |
| cagr | -0.3449 |
| net_avg_win | 67.6379 |
| net_avg_loss | -84.5643 |
| avg_hold_time_bars | 22.9384 |
| exposure | 0.6284 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
