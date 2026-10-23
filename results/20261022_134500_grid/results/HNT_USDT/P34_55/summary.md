# EMA Hourly Continuation — HNT/USDT P34_55

**Symbol:** HNT/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 927 |
| net_profit_factor | 0.3871 |
| net_win_rate | 0.4229 |
| gross_profit_factor | 0.7388 |
| gross_win_rate | 0.4337 |
| sharpe_ratio | -8.5760 |
| sortino_ratio | -3.6977 |
| max_drawdown | 0.9906 |
| cagr | -0.8411 |
| net_avg_win | 15.9564 |
| net_avg_loss | -30.1987 |
| avg_hold_time_bars | 3.1327 |
| exposure | 0.1320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
