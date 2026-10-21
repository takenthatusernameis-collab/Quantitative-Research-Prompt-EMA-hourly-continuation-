# EMA Hourly Continuation — MERL/USDT P8_12

**Symbol:** MERL/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.7359 |
| net_win_rate | 0.4956 |
| gross_profit_factor | 0.9755 |
| gross_win_rate | 0.4956 |
| sharpe_ratio | -1.7712 |
| sortino_ratio | -0.4677 |
| max_drawdown | 0.4167 |
| cagr | -0.1936 |
| net_avg_win | 69.1182 |
| net_avg_loss | -92.2712 |
| avg_hold_time_bars | 4.0855 |
| exposure | 0.0631 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
