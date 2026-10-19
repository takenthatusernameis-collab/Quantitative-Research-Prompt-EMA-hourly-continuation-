# EMA Hourly Continuation — XCN/USDT P21_50

**Symbol:** XCN/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1217 |
| net_profit_factor | 0.3123 |
| net_win_rate | 0.3813 |
| gross_profit_factor | 0.6495 |
| gross_win_rate | 0.4092 |
| sharpe_ratio | -11.4305 |
| sortino_ratio | -5.6281 |
| max_drawdown | 0.9993 |
| cagr | -0.9449 |
| net_avg_win | 9.7818 |
| net_avg_loss | -19.2986 |
| avg_hold_time_bars | 4.1076 |
| exposure | 0.2272 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
