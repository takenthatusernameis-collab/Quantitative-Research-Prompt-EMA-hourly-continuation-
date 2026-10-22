# EMA Hourly Continuation — PUFFER/USDT P26_55

**Symbol:** PUFFER/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.8358 |
| net_win_rate | 0.5200 |
| gross_profit_factor | 1.0683 |
| gross_win_rate | 0.5200 |
| sharpe_ratio | -1.0829 |
| sortino_ratio | -0.3255 |
| max_drawdown | 0.2723 |
| cagr | -0.1408 |
| net_avg_win | 73.7876 |
| net_avg_loss | -95.6366 |
| avg_hold_time_bars | 8.0286 |
| exposure | 0.1590 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
