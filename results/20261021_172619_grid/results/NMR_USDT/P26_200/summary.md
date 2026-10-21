# EMA Hourly Continuation — NMR/USDT P26_200

**Symbol:** NMR/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.8105 |
| net_win_rate | 0.5014 |
| gross_profit_factor | 0.9819 |
| gross_win_rate | 0.5014 |
| sharpe_ratio | -1.1502 |
| sortino_ratio | -0.3098 |
| max_drawdown | 0.3629 |
| cagr | -0.1344 |
| net_avg_win | 73.0568 |
| net_avg_loss | -90.6460 |
| avg_hold_time_bars | 33.8958 |
| exposure | 0.5470 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
