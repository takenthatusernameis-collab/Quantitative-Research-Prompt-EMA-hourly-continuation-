# EMA Hourly Continuation — ALPINE/USDT P89_200

**Symbol:** ALPINE/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.5364 |
| net_win_rate | 0.4596 |
| gross_profit_factor | 0.8757 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -4.0358 |
| sortino_ratio | -1.1922 |
| max_drawdown | 0.7558 |
| cagr | -0.4283 |
| net_avg_win | 43.8551 |
| net_avg_loss | -69.5350 |
| avg_hold_time_bars | 13.0439 |
| exposure | 0.2567 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
