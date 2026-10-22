# EMA Hourly Continuation — XCN/USDT P21_100

**Symbol:** XCN/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 839 |
| net_profit_factor | 0.4813 |
| net_win_rate | 0.4184 |
| gross_profit_factor | 0.8051 |
| gross_win_rate | 0.4315 |
| sharpe_ratio | -7.4094 |
| sortino_ratio | -2.9853 |
| max_drawdown | 0.9774 |
| cagr | -0.7780 |
| net_avg_win | 25.8378 |
| net_avg_loss | -38.6084 |
| avg_hold_time_bars | 10.6901 |
| exposure | 0.4077 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
