# EMA Hourly Continuation — FLIP/USDT P8_144

**Symbol:** FLIP/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.5963 |
| net_win_rate | 0.4472 |
| gross_profit_factor | 0.8399 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -3.4291 |
| sortino_ratio | -0.9701 |
| max_drawdown | 0.6950 |
| cagr | -0.3694 |
| net_avg_win | 55.6651 |
| net_avg_loss | -75.5122 |
| avg_hold_time_bars | 39.0295 |
| exposure | 0.7220 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
