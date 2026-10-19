# EMA Hourly Continuation — ZBCN/USDT P8_26

**Symbol:** ZBCN/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1702 |
| net_profit_factor | 0.4607 |
| net_win_rate | 0.4659 |
| gross_profit_factor | 0.7834 |
| gross_win_rate | 0.4689 |
| sharpe_ratio | -8.4532 |
| sortino_ratio | -4.9298 |
| max_drawdown | 0.9976 |
| cagr | -0.9123 |
| net_avg_win | 10.7471 |
| net_avg_loss | -20.3496 |
| avg_hold_time_bars | 3.2944 |
| exposure | 0.2594 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
