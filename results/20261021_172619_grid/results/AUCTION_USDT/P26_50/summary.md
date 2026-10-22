# EMA Hourly Continuation — AUCTION/USDT P26_50

**Symbol:** AUCTION/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 529 |
| net_profit_factor | 0.5745 |
| net_win_rate | 0.4594 |
| gross_profit_factor | 0.8637 |
| gross_win_rate | 0.4594 |
| sharpe_ratio | -4.3893 |
| sortino_ratio | -1.4341 |
| max_drawdown | 0.8245 |
| cagr | -0.4894 |
| net_avg_win | 45.3656 |
| net_avg_loss | -67.0908 |
| avg_hold_time_bars | 7.3006 |
| exposure | 0.1748 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
