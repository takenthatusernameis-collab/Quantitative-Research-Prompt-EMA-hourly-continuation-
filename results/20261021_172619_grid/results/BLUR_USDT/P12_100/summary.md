# EMA Hourly Continuation — BLUR/USDT P12_100

**Symbol:** BLUR/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.9497 |
| net_win_rate | 0.5430 |
| gross_profit_factor | 1.1726 |
| gross_win_rate | 0.5430 |
| sharpe_ratio | -0.2847 |
| sortino_ratio | -0.0864 |
| max_drawdown | 0.2542 |
| cagr | -0.0455 |
| net_avg_win | 87.2105 |
| net_avg_loss | -109.0989 |
| avg_hold_time_bars | 30.1267 |
| exposure | 0.6026 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
