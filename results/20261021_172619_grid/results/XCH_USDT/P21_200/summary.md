# EMA Hourly Continuation — XCH/USDT P21_200

**Symbol:** XCH/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.8679 |
| net_win_rate | 0.5105 |
| gross_profit_factor | 1.0323 |
| gross_win_rate | 0.5105 |
| sharpe_ratio | -0.8107 |
| sortino_ratio | -0.2273 |
| max_drawdown | 0.2793 |
| cagr | -0.1024 |
| net_avg_win | 80.0524 |
| net_avg_loss | -96.1859 |
| avg_hold_time_bars | 33.7382 |
| exposure | 0.5858 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
