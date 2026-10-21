# EMA Hourly Continuation — SAFE/USDT P20_89

**Symbol:** SAFE/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.8002 |
| net_win_rate | 0.4970 |
| gross_profit_factor | 0.9855 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -1.6091 |
| sortino_ratio | -0.5178 |
| max_drawdown | 0.5097 |
| cagr | -0.2132 |
| net_avg_win | 72.0737 |
| net_avg_loss | -89.0036 |
| avg_hold_time_bars | 15.4553 |
| exposure | 0.3560 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
