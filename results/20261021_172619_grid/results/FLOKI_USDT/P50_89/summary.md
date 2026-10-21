# EMA Hourly Continuation — FLOKI/USDT P50_89

**Symbol:** FLOKI/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.7932 |
| net_win_rate | 0.5114 |
| gross_profit_factor | 1.0413 |
| gross_win_rate | 0.5114 |
| sharpe_ratio | -1.3563 |
| sortino_ratio | -0.3650 |
| max_drawdown | 0.3796 |
| cagr | -0.1544 |
| net_avg_win | 73.6212 |
| net_avg_loss | -97.1615 |
| avg_hold_time_bars | 8.0229 |
| exposure | 0.1276 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
