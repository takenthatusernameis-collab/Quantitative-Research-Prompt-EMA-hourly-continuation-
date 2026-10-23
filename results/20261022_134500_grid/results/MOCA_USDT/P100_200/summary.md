# EMA Hourly Continuation — MOCA/USDT P100_200

**Symbol:** MOCA/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.4687 |
| net_win_rate | 0.4171 |
| gross_profit_factor | 0.7800 |
| gross_win_rate | 0.4365 |
| sharpe_ratio | -5.1032 |
| sortino_ratio | -1.4282 |
| max_drawdown | 0.8066 |
| cagr | -0.5121 |
| net_avg_win | 47.0146 |
| net_avg_loss | -71.7903 |
| avg_hold_time_bars | 8.2983 |
| exposure | 0.1506 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
