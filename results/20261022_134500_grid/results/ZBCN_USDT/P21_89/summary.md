# EMA Hourly Continuation — ZBCN/USDT P21_89

**Symbol:** ZBCN/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 891 |
| net_profit_factor | 0.6199 |
| net_win_rate | 0.4837 |
| gross_profit_factor | 0.9374 |
| gross_win_rate | 0.4871 |
| sharpe_ratio | -4.1382 |
| sortino_ratio | -1.7528 |
| max_drawdown | 0.8825 |
| cagr | -0.5680 |
| net_avg_win | 33.0726 |
| net_avg_loss | -49.9864 |
| avg_hold_time_bars | 7.4848 |
| exposure | 0.3086 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
