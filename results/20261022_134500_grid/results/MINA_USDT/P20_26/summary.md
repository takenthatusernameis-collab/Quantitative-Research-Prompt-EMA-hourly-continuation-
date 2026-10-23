# EMA Hourly Continuation — MINA/USDT P20_26

**Symbol:** MINA/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1247 |
| net_profit_factor | 0.2557 |
| net_win_rate | 0.4010 |
| gross_profit_factor | 0.8550 |
| gross_win_rate | 0.4483 |
| sharpe_ratio | -12.7849 |
| sortino_ratio | -6.5097 |
| max_drawdown | 0.9998 |
| cagr | -0.9642 |
| net_avg_win | 6.8688 |
| net_avg_loss | -17.9814 |
| avg_hold_time_bars | 2.2253 |
| exposure | 0.1261 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
