# EMA Hourly Continuation — XCN/USDT P21_34

**Symbol:** XCN/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1348 |
| net_profit_factor | 0.2382 |
| net_win_rate | 0.3620 |
| gross_profit_factor | 0.6049 |
| gross_win_rate | 0.3924 |
| sharpe_ratio | -14.4759 |
| sortino_ratio | -7.6114 |
| max_drawdown | 1.0000 |
| cagr | -0.9826 |
| net_avg_win | 6.4059 |
| net_avg_loss | -15.2624 |
| avg_hold_time_bars | 2.6491 |
| exposure | 0.1623 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
