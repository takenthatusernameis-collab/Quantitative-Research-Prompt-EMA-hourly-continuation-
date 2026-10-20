# EMA Hourly Continuation — FLIP/USDT P12_26

**Symbol:** FLIP/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 998 |
| net_profit_factor | 0.3172 |
| net_win_rate | 0.3657 |
| gross_profit_factor | 0.8124 |
| gross_win_rate | 0.4198 |
| sharpe_ratio | -11.9082 |
| sortino_ratio | -5.3987 |
| max_drawdown | 0.9992 |
| cagr | -0.9408 |
| net_avg_win | 12.7148 |
| net_avg_loss | -23.1164 |
| avg_hold_time_bars | 5.4679 |
| exposure | 0.2480 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
