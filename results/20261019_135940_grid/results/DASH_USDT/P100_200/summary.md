# EMA Hourly Continuation — DASH/USDT P100_200

**Symbol:** DASH/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 451 |
| net_profit_factor | 0.3334 |
| net_win_rate | 0.4169 |
| gross_profit_factor | 0.6760 |
| gross_win_rate | 0.4324 |
| sharpe_ratio | -5.5935 |
| sortino_ratio | -1.6554 |
| max_drawdown | 0.8811 |
| cagr | -0.5666 |
| net_avg_win | 23.3417 |
| net_avg_loss | -50.0493 |
| avg_hold_time_bars | 6.9180 |
| exposure | 0.1418 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
