# EMA Hourly Continuation — CAKE/USDT P50_100

**Symbol:** CAKE/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 571 |
| net_profit_factor | 0.3858 |
| net_win_rate | 0.4168 |
| gross_profit_factor | 0.7588 |
| gross_win_rate | 0.4466 |
| sharpe_ratio | -6.6818 |
| sortino_ratio | -2.2614 |
| max_drawdown | 0.9453 |
| cagr | -0.6772 |
| net_avg_win | 24.8535 |
| net_avg_loss | -46.0381 |
| avg_hold_time_bars | 6.7933 |
| exposure | 0.1763 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
