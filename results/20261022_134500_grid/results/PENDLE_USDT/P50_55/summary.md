# EMA Hourly Continuation — PENDLE/USDT P50_55

**Symbol:** PENDLE/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 804 |
| net_profit_factor | 0.2525 |
| net_win_rate | 0.3831 |
| gross_profit_factor | 0.6695 |
| gross_win_rate | 0.4142 |
| sharpe_ratio | -10.8556 |
| sortino_ratio | -4.4262 |
| max_drawdown | 0.9973 |
| cagr | -0.9048 |
| net_avg_win | 10.9377 |
| net_avg_loss | -26.8983 |
| avg_hold_time_bars | 2.1070 |
| exposure | 0.0770 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
