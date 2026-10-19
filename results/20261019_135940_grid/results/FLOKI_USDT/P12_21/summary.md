# EMA Hourly Continuation — FLOKI/USDT P12_21

**Symbol:** FLOKI/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1529 |
| net_profit_factor | 0.3321 |
| net_win_rate | 0.3728 |
| gross_profit_factor | 0.6578 |
| gross_win_rate | 0.3983 |
| sharpe_ratio | -14.6093 |
| sortino_ratio | -8.1262 |
| max_drawdown | 1.0000 |
| cagr | -0.9861 |
| net_avg_win | 8.7248 |
| net_avg_loss | -15.6131 |
| avg_hold_time_bars | 2.1910 |
| exposure | 0.1523 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
