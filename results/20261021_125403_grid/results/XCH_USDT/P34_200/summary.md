# EMA Hourly Continuation — XCH/USDT P34_200

**Symbol:** XCH/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.8875 |
| net_win_rate | 0.5172 |
| gross_profit_factor | 1.0602 |
| gross_win_rate | 0.5172 |
| sharpe_ratio | -0.6387 |
| sortino_ratio | -0.1713 |
| max_drawdown | 0.1991 |
| cagr | -0.0791 |
| net_avg_win | 81.9112 |
| net_avg_loss | -98.8887 |
| avg_hold_time_bars | 32.1408 |
| exposure | 0.5084 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
