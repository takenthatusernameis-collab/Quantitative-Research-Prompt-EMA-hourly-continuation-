# EMA Hourly Continuation — CAKE/USDT P12_21

**Symbol:** CAKE/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.8843 |
| net_win_rate | 0.5747 |
| gross_profit_factor | 1.3458 |
| gross_win_rate | 0.5747 |
| sharpe_ratio | -0.6738 |
| sortino_ratio | -0.1725 |
| max_drawdown | 0.3102 |
| cagr | -0.0780 |
| net_avg_win | 79.7407 |
| net_avg_loss | -121.8327 |
| avg_hold_time_bars | 5.3247 |
| exposure | 0.0745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
