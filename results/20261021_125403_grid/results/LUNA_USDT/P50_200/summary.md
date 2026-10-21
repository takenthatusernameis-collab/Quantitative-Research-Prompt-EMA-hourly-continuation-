# EMA Hourly Continuation — LUNA/USDT P50_200

**Symbol:** LUNA/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 312 |
| net_profit_factor | 0.6557 |
| net_win_rate | 0.4519 |
| gross_profit_factor | 0.8128 |
| gross_win_rate | 0.4519 |
| sharpe_ratio | -2.2667 |
| sortino_ratio | -0.5680 |
| max_drawdown | 0.4822 |
| cagr | -0.2305 |
| net_avg_win | 65.1315 |
| net_avg_loss | -81.9016 |
| avg_hold_time_bars | 26.2660 |
| exposure | 0.3725 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
