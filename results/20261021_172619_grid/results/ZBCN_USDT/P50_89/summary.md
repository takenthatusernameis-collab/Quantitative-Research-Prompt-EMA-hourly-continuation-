# EMA Hourly Continuation — ZBCN/USDT P50_89

**Symbol:** ZBCN/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 274 |
| net_profit_factor | 0.8125 |
| net_win_rate | 0.5036 |
| gross_profit_factor | 0.9945 |
| gross_win_rate | 0.5036 |
| sharpe_ratio | -1.0139 |
| sortino_ratio | -0.2424 |
| max_drawdown | 0.3007 |
| cagr | -0.1062 |
| net_avg_win | 75.9712 |
| net_avg_loss | -94.8824 |
| avg_hold_time_bars | 6.1715 |
| exposure | 0.0782 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
