# EMA Hourly Continuation — UNI/USDT P12_50

**Symbol:** UNI/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1104 |
| net_profit_factor | 0.5334 |
| net_win_rate | 0.4638 |
| gross_profit_factor | 0.9391 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -6.6357 |
| sortino_ratio | -3.0970 |
| max_drawdown | 0.9782 |
| cagr | -0.7801 |
| net_avg_win | 21.8329 |
| net_avg_loss | -35.3977 |
| avg_hold_time_bars | 6.4846 |
| exposure | 0.3254 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
