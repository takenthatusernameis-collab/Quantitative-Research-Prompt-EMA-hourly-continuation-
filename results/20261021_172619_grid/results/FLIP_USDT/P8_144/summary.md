# EMA Hourly Continuation — FLIP/USDT P8_144

**Symbol:** FLIP/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.6712 |
| net_win_rate | 0.4571 |
| gross_profit_factor | 0.8533 |
| gross_win_rate | 0.4629 |
| sharpe_ratio | -2.3319 |
| sortino_ratio | -0.6180 |
| max_drawdown | 0.5312 |
| cagr | -0.2471 |
| net_avg_win | 65.0458 |
| net_avg_loss | -81.6026 |
| avg_hold_time_bars | 44.8143 |
| exposure | 0.7130 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
