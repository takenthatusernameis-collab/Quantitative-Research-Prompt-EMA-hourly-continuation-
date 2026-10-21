# EMA Hourly Continuation — XEC/USDT P21_50

**Symbol:** XEC/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 630 |
| net_profit_factor | 0.7038 |
| net_win_rate | 0.4905 |
| gross_profit_factor | 1.0396 |
| gross_win_rate | 0.4905 |
| sharpe_ratio | -3.4364 |
| sortino_ratio | -1.2352 |
| max_drawdown | 0.7969 |
| cagr | -0.4324 |
| net_avg_win | 58.4617 |
| net_avg_loss | -79.9630 |
| avg_hold_time_bars | 7.3524 |
| exposure | 0.2096 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
