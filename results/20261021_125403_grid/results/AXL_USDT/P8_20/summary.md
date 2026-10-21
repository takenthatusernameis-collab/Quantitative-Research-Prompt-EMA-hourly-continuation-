# EMA Hourly Continuation — AXL/USDT P8_20

**Symbol:** AXL/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 664 |
| net_profit_factor | 0.6057 |
| net_win_rate | 0.4367 |
| gross_profit_factor | 0.8099 |
| gross_win_rate | 0.4367 |
| sharpe_ratio | -4.5404 |
| sortino_ratio | -1.6603 |
| max_drawdown | 0.8565 |
| cagr | -0.5348 |
| net_avg_win | 45.2846 |
| net_avg_loss | -57.9722 |
| avg_hold_time_bars | 5.4262 |
| exposure | 0.1630 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
