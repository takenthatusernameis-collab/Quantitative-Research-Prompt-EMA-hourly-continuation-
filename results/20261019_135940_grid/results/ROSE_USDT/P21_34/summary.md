# EMA Hourly Continuation — ROSE/USDT P21_34

**Symbol:** ROSE/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1216 |
| net_profit_factor | 0.3830 |
| net_win_rate | 0.4095 |
| gross_profit_factor | 0.8309 |
| gross_win_rate | 0.4276 |
| sharpe_ratio | -10.9519 |
| sortino_ratio | -5.4281 |
| max_drawdown | 0.9989 |
| cagr | -0.9342 |
| net_avg_win | 12.4504 |
| net_avg_loss | -22.5481 |
| avg_hold_time_bars | 2.6308 |
| exposure | 0.1454 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
