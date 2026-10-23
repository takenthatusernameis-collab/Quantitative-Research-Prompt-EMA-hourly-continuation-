# EMA Hourly Continuation — ORCA/USDT P21_34

**Symbol:** ORCA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1014 |
| net_profit_factor | 0.4759 |
| net_win_rate | 0.4359 |
| gross_profit_factor | 0.9680 |
| gross_win_rate | 0.4684 |
| sharpe_ratio | -8.5530 |
| sortino_ratio | -3.8491 |
| max_drawdown | 0.9923 |
| cagr | -0.8544 |
| net_avg_win | 20.3825 |
| net_avg_loss | -33.0942 |
| avg_hold_time_bars | 3.4260 |
| exposure | 0.1579 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
