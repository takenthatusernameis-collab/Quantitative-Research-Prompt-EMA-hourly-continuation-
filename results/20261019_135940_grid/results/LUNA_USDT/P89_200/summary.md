# EMA Hourly Continuation — LUNA/USDT P89_200

**Symbol:** LUNA/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.4615 |
| net_win_rate | 0.4270 |
| gross_profit_factor | 0.7525 |
| gross_win_rate | 0.4358 |
| sharpe_ratio | -4.9545 |
| sortino_ratio | -1.4957 |
| max_drawdown | 0.8323 |
| cagr | -0.5089 |
| net_avg_win | 36.9562 |
| net_avg_loss | -59.6741 |
| avg_hold_time_bars | 10.9027 |
| exposure | 0.2240 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
