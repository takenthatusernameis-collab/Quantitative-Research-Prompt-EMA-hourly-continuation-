# EMA Hourly Continuation — W/USDT P21_100

**Symbol:** W/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.7398 |
| net_win_rate | 0.5015 |
| gross_profit_factor | 1.0583 |
| gross_win_rate | 0.5090 |
| sharpe_ratio | -2.7320 |
| sortino_ratio | -0.9958 |
| max_drawdown | 0.7302 |
| cagr | -0.3776 |
| net_avg_win | 58.9130 |
| net_avg_loss | -80.1064 |
| avg_hold_time_bars | 13.8299 |
| exposure | 0.4212 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
