# EMA Hourly Continuation — ATOM/USDT P50_55

**Symbol:** ATOM/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 81 |
| net_profit_factor | 0.7867 |
| net_win_rate | 0.5432 |
| gross_profit_factor | 1.1746 |
| gross_win_rate | 0.5432 |
| sharpe_ratio | -0.6314 |
| sortino_ratio | -0.0825 |
| max_drawdown | 0.1058 |
| cagr | -0.0370 |
| net_avg_win | 75.6209 |
| net_avg_loss | -114.3154 |
| avg_hold_time_bars | 5.5432 |
| exposure | 0.0204 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
