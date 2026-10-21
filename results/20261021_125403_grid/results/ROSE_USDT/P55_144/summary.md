# EMA Hourly Continuation — ROSE/USDT P55_144

**Symbol:** ROSE/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.8723 |
| net_win_rate | 0.5194 |
| gross_profit_factor | 1.0685 |
| gross_win_rate | 0.5194 |
| sharpe_ratio | -0.7550 |
| sortino_ratio | -0.2062 |
| max_drawdown | 0.2523 |
| cagr | -0.0932 |
| net_avg_win | 79.5415 |
| net_avg_loss | -98.5661 |
| avg_hold_time_bars | 15.0389 |
| exposure | 0.2461 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
