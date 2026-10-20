# EMA Hourly Continuation — OSMO/USDT P100_200

**Symbol:** OSMO/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.5244 |
| net_win_rate | 0.4454 |
| gross_profit_factor | 0.8250 |
| gross_win_rate | 0.4454 |
| sharpe_ratio | -3.8005 |
| sortino_ratio | -1.0180 |
| max_drawdown | 0.7076 |
| cagr | -0.3825 |
| net_avg_win | 48.6716 |
| net_avg_loss | -74.5393 |
| avg_hold_time_bars | 10.4594 |
| exposure | 0.1697 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
