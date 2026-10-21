# EMA Hourly Continuation — XCN/USDT P12_20

**Symbol:** XCN/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 227 |
| net_profit_factor | 0.6103 |
| net_win_rate | 0.4537 |
| gross_profit_factor | 0.8658 |
| gross_win_rate | 0.4537 |
| sharpe_ratio | -2.5079 |
| sortino_ratio | -0.5391 |
| max_drawdown | 0.4726 |
| cagr | -0.2194 |
| net_avg_win | 70.4289 |
| net_avg_loss | -95.8578 |
| avg_hold_time_bars | 6.1850 |
| exposure | 0.0638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
