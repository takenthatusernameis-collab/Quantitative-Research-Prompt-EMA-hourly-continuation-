# EMA Hourly Continuation — ZIL/USDT P12_50

**Symbol:** ZIL/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1032 |
| net_profit_factor | 0.4946 |
| net_win_rate | 0.4409 |
| gross_profit_factor | 0.8910 |
| gross_win_rate | 0.4612 |
| sharpe_ratio | -7.4558 |
| sortino_ratio | -3.3750 |
| max_drawdown | 0.9854 |
| cagr | -0.8066 |
| net_avg_win | 21.1598 |
| net_avg_loss | -33.7369 |
| avg_hold_time_bars | 7.8014 |
| exposure | 0.3660 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
