# EMA Hourly Continuation — VELO/USDT P26_50

**Symbol:** VELO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1009 |
| net_profit_factor | 0.5092 |
| net_win_rate | 0.4470 |
| gross_profit_factor | 0.8019 |
| gross_win_rate | 0.4569 |
| sharpe_ratio | -6.9906 |
| sortino_ratio | -3.1340 |
| max_drawdown | 0.9786 |
| cagr | -0.7789 |
| net_avg_win | 22.4817 |
| net_avg_loss | -35.6867 |
| avg_hold_time_bars | 3.3925 |
| exposure | 0.1556 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
