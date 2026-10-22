# EMA Hourly Continuation — VET/USDT P50_55

**Symbol:** VET/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 813 |
| net_profit_factor | 0.1888 |
| net_win_rate | 0.3346 |
| gross_profit_factor | 0.7672 |
| gross_win_rate | 0.4121 |
| sharpe_ratio | -13.2011 |
| sortino_ratio | -5.6188 |
| max_drawdown | 0.9996 |
| cagr | -0.9533 |
| net_avg_win | 8.5546 |
| net_avg_loss | -22.7769 |
| avg_hold_time_bars | 1.7601 |
| exposure | 0.0650 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
