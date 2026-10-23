# EMA Hourly Continuation — ARKM/USDT P34_55

**Symbol:** ARKM/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 902 |
| net_profit_factor | 0.5030 |
| net_win_rate | 0.4412 |
| gross_profit_factor | 0.8716 |
| gross_win_rate | 0.4512 |
| sharpe_ratio | -7.3494 |
| sortino_ratio | -3.1225 |
| max_drawdown | 0.9796 |
| cagr | -0.7807 |
| net_avg_win | 24.8627 |
| net_avg_loss | -39.0356 |
| avg_hold_time_bars | 3.0399 |
| exposure | 0.1246 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
