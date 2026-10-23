# EMA Hourly Continuation — NMR/USDT P26_89

**Symbol:** NMR/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 758 |
| net_profit_factor | 0.6973 |
| net_win_rate | 0.4934 |
| gross_profit_factor | 1.0671 |
| gross_win_rate | 0.5026 |
| sharpe_ratio | -4.1162 |
| sortino_ratio | -1.5919 |
| max_drawdown | 0.8652 |
| cagr | -0.5345 |
| net_avg_win | 52.5772 |
| net_avg_loss | -73.4327 |
| avg_hold_time_bars | 9.8430 |
| exposure | 0.3391 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
