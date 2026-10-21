# EMA Hourly Continuation — FIL/USDT P8_20

**Symbol:** FIL/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.7610 |
| net_win_rate | 0.5231 |
| gross_profit_factor | 1.0743 |
| gross_win_rate | 0.5231 |
| sharpe_ratio | -1.6837 |
| sortino_ratio | -0.5185 |
| max_drawdown | 0.5061 |
| cagr | -0.2112 |
| net_avg_win | 60.0592 |
| net_avg_loss | -86.5545 |
| avg_hold_time_bars | 5.6088 |
| exposure | 0.1160 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
