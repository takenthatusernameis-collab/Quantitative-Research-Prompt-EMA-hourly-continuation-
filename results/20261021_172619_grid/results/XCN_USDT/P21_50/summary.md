# EMA Hourly Continuation — XCN/USDT P21_50

**Symbol:** XCN/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.6746 |
| net_win_rate | 0.4736 |
| gross_profit_factor | 0.9021 |
| gross_win_rate | 0.4736 |
| sharpe_ratio | -2.6781 |
| sortino_ratio | -0.8147 |
| max_drawdown | 0.6202 |
| cagr | -0.3125 |
| net_avg_win | 58.7842 |
| net_avg_loss | -78.3934 |
| avg_hold_time_bars | 7.9361 |
| exposure | 0.1638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
