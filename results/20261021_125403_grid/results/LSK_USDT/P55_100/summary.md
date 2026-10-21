# EMA Hourly Continuation — LSK/USDT P55_100

**Symbol:** LSK/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.6297 |
| net_win_rate | 0.4826 |
| gross_profit_factor | 0.9041 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -2.7980 |
| sortino_ratio | -0.8311 |
| max_drawdown | 0.6387 |
| cagr | -0.3183 |
| net_avg_win | 50.5180 |
| net_avg_loss | -74.8320 |
| avg_hold_time_bars | 7.4780 |
| exposure | 0.1465 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
