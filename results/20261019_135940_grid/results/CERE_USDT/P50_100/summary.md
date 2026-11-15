# EMA Hourly Continuation — CERE/USDT P50_100

**Symbol:** CERE/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 708 |
| net_profit_factor | 0.4346 |
| net_win_rate | 0.3333 |
| gross_profit_factor | 0.8286 |
| gross_win_rate | 0.3602 |
| sharpe_ratio | -10.5407 |
| sortino_ratio | -4.0286 |
| max_drawdown | 0.9951 |
| cagr | -0.8792 |
| net_avg_win | 32.4124 |
| net_avg_loss | -37.2877 |
| avg_hold_time_bars | 6.5918 |
| exposure | 0.2121 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
