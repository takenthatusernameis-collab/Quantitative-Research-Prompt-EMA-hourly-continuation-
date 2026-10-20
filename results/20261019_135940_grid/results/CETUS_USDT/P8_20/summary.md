# EMA Hourly Continuation — CETUS/USDT P8_20

**Symbol:** CETUS/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1642 |
| net_profit_factor | 0.4816 |
| net_win_rate | 0.4367 |
| gross_profit_factor | 0.9445 |
| gross_win_rate | 0.4537 |
| sharpe_ratio | -10.9016 |
| sortino_ratio | -6.1526 |
| max_drawdown | 0.9996 |
| cagr | -0.9567 |
| net_avg_win | 12.9514 |
| net_avg_loss | -20.8460 |
| avg_hold_time_bars | 3.0037 |
| exposure | 0.2232 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
