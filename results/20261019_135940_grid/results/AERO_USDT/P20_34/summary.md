# EMA Hourly Continuation — AERO/USDT P20_34

**Symbol:** AERO/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1040 |
| net_profit_factor | 0.3298 |
| net_win_rate | 0.4365 |
| gross_profit_factor | 0.6517 |
| gross_win_rate | 0.4529 |
| sharpe_ratio | -8.8183 |
| sortino_ratio | -4.0260 |
| max_drawdown | 0.9938 |
| cagr | -0.8666 |
| net_avg_win | 10.7711 |
| net_avg_loss | -25.3013 |
| avg_hold_time_bars | 2.6240 |
| exposure | 0.1240 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
