# EMA Hourly Continuation — ARKM/USDT P21_26

**Symbol:** ARKM/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1235 |
| net_profit_factor | 0.3216 |
| net_win_rate | 0.3733 |
| gross_profit_factor | 0.7453 |
| gross_win_rate | 0.4073 |
| sharpe_ratio | -13.7136 |
| sortino_ratio | -6.9833 |
| max_drawdown | 0.9999 |
| cagr | -0.9733 |
| net_avg_win | 10.2802 |
| net_avg_loss | -19.0414 |
| avg_hold_time_bars | 1.7660 |
| exposure | 0.0991 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
