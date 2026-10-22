# EMA Hourly Continuation — SLP/USDT P8_12

**Symbol:** SLP/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.6478 |
| net_win_rate | 0.4815 |
| gross_profit_factor | 0.9430 |
| gross_win_rate | 0.4815 |
| sharpe_ratio | -2.6382 |
| sortino_ratio | -0.7096 |
| max_drawdown | 0.5560 |
| cagr | -0.2762 |
| net_avg_win | 60.4992 |
| net_avg_loss | -86.7253 |
| avg_hold_time_bars | 4.1937 |
| exposure | 0.0669 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
