# EMA Hourly Continuation — LUNA/USDT P34_55

**Symbol:** LUNA/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.7660 |
| net_win_rate | 0.5136 |
| gross_profit_factor | 1.0542 |
| gross_win_rate | 0.5136 |
| sharpe_ratio | -1.3324 |
| sortino_ratio | -0.3077 |
| max_drawdown | 0.3143 |
| cagr | -0.1314 |
| net_avg_win | 73.8921 |
| net_avg_loss | -101.8714 |
| avg_hold_time_bars | 5.6926 |
| exposure | 0.0665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
