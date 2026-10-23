# EMA Hourly Continuation — AEVO/USDT P8_21

**Symbol:** AEVO/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1598 |
| net_profit_factor | 0.4837 |
| net_win_rate | 0.4506 |
| gross_profit_factor | 0.8813 |
| gross_win_rate | 0.4681 |
| sharpe_ratio | -9.5715 |
| sortino_ratio | -5.3590 |
| max_drawdown | 0.9988 |
| cagr | -0.9301 |
| net_avg_win | 12.9973 |
| net_avg_loss | -22.0341 |
| avg_hold_time_bars | 3.5006 |
| exposure | 0.2531 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
