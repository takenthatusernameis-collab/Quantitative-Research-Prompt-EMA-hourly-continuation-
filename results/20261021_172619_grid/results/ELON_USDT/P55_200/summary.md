# EMA Hourly Continuation — ELON/USDT P55_200

**Symbol:** ELON/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.6452 |
| net_win_rate | 0.4530 |
| gross_profit_factor | 0.8092 |
| gross_win_rate | 0.4530 |
| sharpe_ratio | -2.2636 |
| sortino_ratio | -0.5548 |
| max_drawdown | 0.4855 |
| cagr | -0.2247 |
| net_avg_win | 63.6346 |
| net_avg_loss | -81.6795 |
| avg_hold_time_bars | 25.4463 |
| exposure | 0.3447 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
