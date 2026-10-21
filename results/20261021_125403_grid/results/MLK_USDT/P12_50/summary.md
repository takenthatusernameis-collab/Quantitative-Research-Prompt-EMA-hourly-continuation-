# EMA Hourly Continuation — MLK/USDT P12_50

**Symbol:** MLK/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 554 |
| net_profit_factor | 0.4793 |
| net_win_rate | 0.3863 |
| gross_profit_factor | 0.6882 |
| gross_win_rate | 0.3899 |
| sharpe_ratio | -5.6846 |
| sortino_ratio | -1.8859 |
| max_drawdown | 0.8949 |
| cagr | -0.5846 |
| net_avg_win | 38.3258 |
| net_avg_loss | -50.3266 |
| avg_hold_time_bars | 11.6895 |
| exposure | 0.2931 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
