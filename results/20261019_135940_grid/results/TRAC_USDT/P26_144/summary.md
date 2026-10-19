# EMA Hourly Continuation — TRAC/USDT P26_144

**Symbol:** TRAC/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.7126 |
| net_win_rate | 0.4850 |
| gross_profit_factor | 0.9918 |
| gross_win_rate | 0.4910 |
| sharpe_ratio | -2.6902 |
| sortino_ratio | -0.8431 |
| max_drawdown | 0.6475 |
| cagr | -0.3316 |
| net_avg_win | 65.1947 |
| net_avg_loss | -86.1530 |
| avg_hold_time_bars | 19.6974 |
| exposure | 0.4468 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
