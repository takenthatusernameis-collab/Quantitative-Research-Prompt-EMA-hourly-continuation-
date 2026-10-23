# EMA Hourly Continuation — MLK/USDT P55_89

**Symbol:** MLK/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 908 |
| net_profit_factor | 0.2045 |
| net_win_rate | 0.2412 |
| gross_profit_factor | 0.4714 |
| gross_win_rate | 0.2522 |
| sharpe_ratio | -15.0955 |
| sortino_ratio | -6.6406 |
| max_drawdown | 0.9999 |
| cagr | -0.9697 |
| net_avg_win | 11.7379 |
| net_avg_loss | -18.2426 |
| avg_hold_time_bars | 3.7148 |
| exposure | 0.1526 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
