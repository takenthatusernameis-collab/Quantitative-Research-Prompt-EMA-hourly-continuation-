# EMA Hourly Continuation — XCN/USDT P26_200

**Symbol:** XCN/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.6097 |
| net_win_rate | 0.4674 |
| gross_profit_factor | 0.9121 |
| gross_win_rate | 0.4695 |
| sharpe_ratio | -3.5646 |
| sortino_ratio | -1.0888 |
| max_drawdown | 0.7351 |
| cagr | -0.4084 |
| net_avg_win | 51.5325 |
| net_avg_loss | -74.1645 |
| avg_hold_time_bars | 27.3116 |
| exposure | 0.5897 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
