# EMA Hourly Continuation — FLOW/USDT P21_55

**Symbol:** FLOW/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 954 |
| net_profit_factor | 0.4510 |
| net_win_rate | 0.4308 |
| gross_profit_factor | 0.8489 |
| gross_win_rate | 0.4476 |
| sharpe_ratio | -7.7914 |
| sortino_ratio | -3.3931 |
| max_drawdown | 0.9851 |
| cagr | -0.8107 |
| net_avg_win | 19.6801 |
| net_avg_loss | -33.0304 |
| avg_hold_time_bars | 5.3134 |
| exposure | 0.2304 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
