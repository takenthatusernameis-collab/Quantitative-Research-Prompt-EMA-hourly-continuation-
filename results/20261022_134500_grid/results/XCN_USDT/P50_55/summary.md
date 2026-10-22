# EMA Hourly Continuation — XCN/USDT P50_55

**Symbol:** XCN/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 988 |
| net_profit_factor | 0.1277 |
| net_win_rate | 0.2834 |
| gross_profit_factor | 0.6408 |
| gross_win_rate | 0.3421 |
| sharpe_ratio | -16.1690 |
| sortino_ratio | -7.6801 |
| max_drawdown | 1.0000 |
| cagr | -0.9865 |
| net_avg_win | 5.2294 |
| net_avg_loss | -16.1921 |
| avg_hold_time_bars | 1.9393 |
| exposure | 0.0871 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
