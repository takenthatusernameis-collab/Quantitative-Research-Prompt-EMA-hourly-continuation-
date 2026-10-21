# EMA Hourly Continuation — ORDI/USDT P20_21

**Symbol:** ORDI/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 146 |
| net_profit_factor | 0.6754 |
| net_win_rate | 0.4795 |
| gross_profit_factor | 0.9137 |
| gross_win_rate | 0.4795 |
| sharpe_ratio | -1.4578 |
| sortino_ratio | -0.2521 |
| max_drawdown | 0.2532 |
| cagr | -0.1098 |
| net_avg_win | 75.2614 |
| net_avg_loss | -102.6349 |
| avg_hold_time_bars | 4.9315 |
| exposure | 0.0327 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
