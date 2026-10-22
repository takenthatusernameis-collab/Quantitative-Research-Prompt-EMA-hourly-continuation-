# EMA Hourly Continuation — AAVE/USDT P26_55

**Symbol:** AAVE/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 927 |
| net_profit_factor | 0.4560 |
| net_win_rate | 0.4261 |
| gross_profit_factor | 0.8492 |
| gross_win_rate | 0.4401 |
| sharpe_ratio | -8.3360 |
| sortino_ratio | -3.5680 |
| max_drawdown | 0.9891 |
| cagr | -0.8335 |
| net_avg_win | 20.9839 |
| net_avg_loss | -34.1688 |
| avg_hold_time_bars | 3.9396 |
| exposure | 0.1660 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
