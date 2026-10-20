# EMA Hourly Continuation — CATI/USDT P55_200

**Symbol:** CATI/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.5595 |
| net_win_rate | 0.4432 |
| gross_profit_factor | 0.8741 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -4.2048 |
| sortino_ratio | -1.2486 |
| max_drawdown | 0.7291 |
| cagr | -0.4516 |
| net_avg_win | 55.2746 |
| net_avg_loss | -78.6526 |
| avg_hold_time_bars | 19.0054 |
| exposure | 0.3855 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
