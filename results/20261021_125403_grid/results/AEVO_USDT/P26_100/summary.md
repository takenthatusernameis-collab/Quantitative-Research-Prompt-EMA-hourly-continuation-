# EMA Hourly Continuation — AEVO/USDT P26_100

**Symbol:** AEVO/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.7663 |
| net_win_rate | 0.4887 |
| gross_profit_factor | 0.9530 |
| gross_win_rate | 0.4887 |
| sharpe_ratio | -1.8811 |
| sortino_ratio | -0.5915 |
| max_drawdown | 0.5184 |
| cagr | -0.2386 |
| net_avg_win | 68.5201 |
| net_avg_loss | -85.4644 |
| avg_hold_time_bars | 16.1889 |
| exposure | 0.3568 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
