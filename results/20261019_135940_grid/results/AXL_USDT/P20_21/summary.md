# EMA Hourly Continuation — AXL/USDT P20_21

**Symbol:** AXL/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1309 |
| net_profit_factor | 0.2150 |
| net_win_rate | 0.3048 |
| gross_profit_factor | 0.8030 |
| gross_win_rate | 0.3789 |
| sharpe_ratio | -17.1460 |
| sortino_ratio | -9.1375 |
| max_drawdown | 1.0000 |
| cagr | -0.9933 |
| net_avg_win | 6.8625 |
| net_avg_loss | -13.9979 |
| avg_hold_time_bars | 2.0061 |
| exposure | 0.1188 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
