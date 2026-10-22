# EMA Hourly Continuation — XCN/USDT P26_34

**Symbol:** XCN/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1299 |
| net_profit_factor | 0.1901 |
| net_win_rate | 0.3333 |
| gross_profit_factor | 0.6039 |
| gross_win_rate | 0.3764 |
| sharpe_ratio | -15.8966 |
| sortino_ratio | -8.3248 |
| max_drawdown | 1.0000 |
| cagr | -0.9892 |
| net_avg_win | 5.4213 |
| net_avg_loss | -14.2579 |
| avg_hold_time_bars | 2.1139 |
| exposure | 0.1248 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
