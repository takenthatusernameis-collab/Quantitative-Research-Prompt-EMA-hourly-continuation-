# EMA Hourly Continuation — ROSE/USDT P21_144

**Symbol:** ROSE/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.7419 |
| net_win_rate | 0.4935 |
| gross_profit_factor | 1.0129 |
| gross_win_rate | 0.5022 |
| sharpe_ratio | -2.1379 |
| sortino_ratio | -0.6437 |
| max_drawdown | 0.5743 |
| cagr | -0.2669 |
| net_avg_win | 68.2527 |
| net_avg_loss | -89.6384 |
| avg_hold_time_bars | 27.4286 |
| exposure | 0.5760 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
