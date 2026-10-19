# EMA Hourly Continuation — XCN/USDT P8_50

**Symbol:** XCN/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1375 |
| net_profit_factor | 0.3747 |
| net_win_rate | 0.4138 |
| gross_profit_factor | 0.6630 |
| gross_win_rate | 0.4284 |
| sharpe_ratio | -10.0106 |
| sortino_ratio | -5.1720 |
| max_drawdown | 0.9987 |
| cagr | -0.9287 |
| net_avg_win | 10.5177 |
| net_avg_loss | -19.8157 |
| avg_hold_time_bars | 7.0931 |
| exposure | 0.4433 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
