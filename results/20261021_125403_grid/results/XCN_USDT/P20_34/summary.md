# EMA Hourly Continuation — XCN/USDT P20_34

**Symbol:** XCN/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 283 |
| net_profit_factor | 0.6990 |
| net_win_rate | 0.4947 |
| gross_profit_factor | 0.9897 |
| gross_win_rate | 0.4947 |
| sharpe_ratio | -1.9637 |
| sortino_ratio | -0.4742 |
| max_drawdown | 0.4246 |
| cagr | -0.1947 |
| net_avg_win | 69.5789 |
| net_avg_loss | -97.4582 |
| avg_hold_time_bars | 6.3004 |
| exposure | 0.0810 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
