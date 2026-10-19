# EMA Hourly Continuation — ETC/USDT P12_26

**Symbol:** ETC/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1432 |
| net_profit_factor | 0.3201 |
| net_win_rate | 0.3959 |
| gross_profit_factor | 0.9359 |
| gross_win_rate | 0.4413 |
| sharpe_ratio | -14.0366 |
| sortino_ratio | -7.6267 |
| max_drawdown | 1.0000 |
| cagr | -0.9810 |
| net_avg_win | 8.3018 |
| net_avg_loss | -17.0019 |
| avg_hold_time_bars | 2.7563 |
| exposure | 0.1794 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
