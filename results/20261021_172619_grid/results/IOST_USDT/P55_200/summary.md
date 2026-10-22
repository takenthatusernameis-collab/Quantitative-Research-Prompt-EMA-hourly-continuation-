# EMA Hourly Continuation — IOST/USDT P55_200

**Symbol:** IOST/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.9733 |
| net_win_rate | 0.5604 |
| gross_profit_factor | 1.2597 |
| gross_win_rate | 0.5604 |
| sharpe_ratio | -0.0947 |
| sortino_ratio | -0.0248 |
| max_drawdown | 0.1993 |
| cagr | -0.0170 |
| net_avg_win | 84.8328 |
| net_avg_loss | -111.0953 |
| avg_hold_time_bars | 22.8854 |
| exposure | 0.3360 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
