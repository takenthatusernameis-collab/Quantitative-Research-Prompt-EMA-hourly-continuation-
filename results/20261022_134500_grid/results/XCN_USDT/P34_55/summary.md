# EMA Hourly Continuation — XCN/USDT P34_55

**Symbol:** XCN/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1054 |
| net_profit_factor | 0.2826 |
| net_win_rate | 0.3615 |
| gross_profit_factor | 0.7022 |
| gross_win_rate | 0.3909 |
| sharpe_ratio | -12.1389 |
| sortino_ratio | -5.6348 |
| max_drawdown | 0.9994 |
| cagr | -0.9470 |
| net_avg_win | 10.3308 |
| net_avg_loss | -20.6981 |
| avg_hold_time_bars | 2.9810 |
| exposure | 0.1428 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
