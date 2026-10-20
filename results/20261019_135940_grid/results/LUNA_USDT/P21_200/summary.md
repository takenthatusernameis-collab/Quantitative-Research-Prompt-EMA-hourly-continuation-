# EMA Hourly Continuation — LUNA/USDT P21_200

**Symbol:** LUNA/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.6334 |
| net_win_rate | 0.4733 |
| gross_profit_factor | 0.9492 |
| gross_win_rate | 0.4822 |
| sharpe_ratio | -3.2749 |
| sortino_ratio | -0.9752 |
| max_drawdown | 0.7056 |
| cagr | -0.3755 |
| net_avg_win | 56.2379 |
| net_avg_loss | -79.8001 |
| avg_hold_time_bars | 29.1178 |
| exposure | 0.5956 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
