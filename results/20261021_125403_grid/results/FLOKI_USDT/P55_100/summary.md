# EMA Hourly Continuation — FLOKI/USDT P55_100

**Symbol:** FLOKI/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.7834 |
| net_win_rate | 0.5084 |
| gross_profit_factor | 1.0178 |
| gross_win_rate | 0.5084 |
| sharpe_ratio | -1.3770 |
| sortino_ratio | -0.3745 |
| max_drawdown | 0.3556 |
| cagr | -0.1580 |
| net_avg_win | 69.7122 |
| net_avg_loss | -92.0168 |
| avg_hold_time_bars | 9.0279 |
| exposure | 0.1469 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
