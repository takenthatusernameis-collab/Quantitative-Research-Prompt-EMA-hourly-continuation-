# EMA Hourly Continuation — ZBCN/USDT P50_55

**Symbol:** ZBCN/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 77 |
| net_profit_factor | 0.7914 |
| net_win_rate | 0.5065 |
| gross_profit_factor | 0.9957 |
| gross_win_rate | 0.5065 |
| sharpe_ratio | -0.6103 |
| sortino_ratio | -0.0772 |
| max_drawdown | 0.1099 |
| cagr | -0.0350 |
| net_avg_win | 81.7700 |
| net_avg_loss | -106.0449 |
| avg_hold_time_bars | 5.0649 |
| exposure | 0.0180 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
