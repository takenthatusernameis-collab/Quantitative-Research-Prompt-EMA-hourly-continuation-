# EMA Hourly Continuation — XPR/USDT P21_50

**Symbol:** XPR/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 871 |
| net_profit_factor | 0.3582 |
| net_win_rate | 0.4030 |
| gross_profit_factor | 0.7377 |
| gross_win_rate | 0.4179 |
| sharpe_ratio | -9.6882 |
| sortino_ratio | -4.0406 |
| max_drawdown | 0.9953 |
| cagr | -0.8796 |
| net_avg_win | 15.8212 |
| net_avg_loss | -29.8156 |
| avg_hold_time_bars | 5.1343 |
| exposure | 0.2033 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
