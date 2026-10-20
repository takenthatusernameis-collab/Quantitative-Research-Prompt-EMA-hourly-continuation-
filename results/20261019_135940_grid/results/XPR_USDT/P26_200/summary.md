# EMA Hourly Continuation — XPR/USDT P26_200

**Symbol:** XPR/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.5124 |
| net_win_rate | 0.4539 |
| gross_profit_factor | 0.7865 |
| gross_win_rate | 0.4610 |
| sharpe_ratio | -3.7059 |
| sortino_ratio | -1.0639 |
| max_drawdown | 0.7374 |
| cagr | -0.4065 |
| net_avg_win | 39.9663 |
| net_avg_loss | -64.8318 |
| avg_hold_time_bars | 27.5910 |
| exposure | 0.5305 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
