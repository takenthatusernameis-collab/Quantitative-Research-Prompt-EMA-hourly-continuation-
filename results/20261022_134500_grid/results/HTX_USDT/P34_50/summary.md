# EMA Hourly Continuation — HTX/USDT P34_50

**Symbol:** HTX/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1036 |
| net_profit_factor | 0.0694 |
| net_win_rate | 0.2056 |
| gross_profit_factor | 0.3459 |
| gross_win_rate | 0.3108 |
| sharpe_ratio | -19.2763 |
| sortino_ratio | -9.9070 |
| max_drawdown | 1.0000 |
| cagr | -0.9957 |
| net_avg_win | 3.5015 |
| net_avg_loss | -13.0569 |
| avg_hold_time_bars | 3.2751 |
| exposure | 0.1535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
