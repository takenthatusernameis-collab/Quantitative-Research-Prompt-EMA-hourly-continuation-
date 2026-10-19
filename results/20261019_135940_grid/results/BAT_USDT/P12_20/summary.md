# EMA Hourly Continuation — BAT/USDT P12_20

**Symbol:** BAT/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1428 |
| net_profit_factor | 0.1661 |
| net_win_rate | 0.3810 |
| gross_profit_factor | 0.5957 |
| gross_win_rate | 0.4356 |
| sharpe_ratio | -14.1894 |
| sortino_ratio | -7.7223 |
| max_drawdown | 1.0000 |
| cagr | -0.9810 |
| net_avg_win | 3.6616 |
| net_avg_loss | -13.5650 |
| avg_hold_time_bars | 2.6078 |
| exposure | 0.1693 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
