# EMA Hourly Continuation — GALA/USDT P50_144

**Symbol:** GALA/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 315 |
| net_profit_factor | 0.6987 |
| net_win_rate | 0.4635 |
| gross_profit_factor | 0.8544 |
| gross_win_rate | 0.4635 |
| sharpe_ratio | -1.9385 |
| sortino_ratio | -0.4890 |
| max_drawdown | 0.4594 |
| cagr | -0.2015 |
| net_avg_win | 68.5477 |
| net_avg_loss | -84.7604 |
| avg_hold_time_bars | 22.3683 |
| exposure | 0.3203 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
