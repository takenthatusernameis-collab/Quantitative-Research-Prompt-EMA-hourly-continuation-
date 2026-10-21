# EMA Hourly Continuation — XCN/USDT P50_55

**Symbol:** XCN/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 105 |
| net_profit_factor | 0.7235 |
| net_win_rate | 0.5048 |
| gross_profit_factor | 1.0275 |
| gross_win_rate | 0.5048 |
| sharpe_ratio | -1.0619 |
| sortino_ratio | -0.1564 |
| max_drawdown | 0.2276 |
| cagr | -0.0688 |
| net_avg_win | 80.8878 |
| net_avg_loss | -113.9466 |
| avg_hold_time_bars | 7.0762 |
| exposure | 0.0338 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
