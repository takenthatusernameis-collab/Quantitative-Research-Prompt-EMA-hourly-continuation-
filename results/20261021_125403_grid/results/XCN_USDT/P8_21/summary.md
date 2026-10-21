# EMA Hourly Continuation — XCN/USDT P8_21

**Symbol:** XCN/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.6463 |
| net_win_rate | 0.4686 |
| gross_profit_factor | 0.8966 |
| gross_win_rate | 0.4686 |
| sharpe_ratio | -3.0188 |
| sortino_ratio | -0.9102 |
| max_drawdown | 0.6490 |
| cagr | -0.3409 |
| net_avg_win | 56.7308 |
| net_avg_loss | -77.4127 |
| avg_hold_time_bars | 6.8543 |
| exposure | 0.1390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
