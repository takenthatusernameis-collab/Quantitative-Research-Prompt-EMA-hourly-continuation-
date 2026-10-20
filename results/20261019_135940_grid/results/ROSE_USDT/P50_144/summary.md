# EMA Hourly Continuation — ROSE/USDT P50_144

**Symbol:** ROSE/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.6924 |
| net_win_rate | 0.4980 |
| gross_profit_factor | 0.9929 |
| gross_win_rate | 0.5041 |
| sharpe_ratio | -2.5243 |
| sortino_ratio | -0.7863 |
| max_drawdown | 0.6187 |
| cagr | -0.3135 |
| net_avg_win | 56.3739 |
| net_avg_loss | -80.7587 |
| avg_hold_time_bars | 13.2347 |
| exposure | 0.2948 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
