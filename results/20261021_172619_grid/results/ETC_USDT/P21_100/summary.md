# EMA Hourly Continuation — ETC/USDT P21_100

**Symbol:** ETC/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.6951 |
| net_win_rate | 0.4885 |
| gross_profit_factor | 0.9580 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -2.5025 |
| sortino_ratio | -0.7834 |
| max_drawdown | 0.6073 |
| cagr | -0.3016 |
| net_avg_win | 57.8778 |
| net_avg_loss | -79.5238 |
| avg_hold_time_bars | 16.5658 |
| exposure | 0.3607 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
