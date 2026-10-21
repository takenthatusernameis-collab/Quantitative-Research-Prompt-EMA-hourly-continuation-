# EMA Hourly Continuation — AVAX/USDT P12_55

**Symbol:** AVAX/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 585 |
| net_profit_factor | 0.7501 |
| net_win_rate | 0.4803 |
| gross_profit_factor | 0.9639 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -2.5977 |
| sortino_ratio | -0.8970 |
| max_drawdown | 0.6869 |
| cagr | -0.3380 |
| net_avg_win | 68.9264 |
| net_avg_loss | -84.9321 |
| avg_hold_time_bars | 12.4991 |
| exposure | 0.3324 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
