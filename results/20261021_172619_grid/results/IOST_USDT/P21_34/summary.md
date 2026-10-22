# EMA Hourly Continuation — IOST/USDT P21_34

**Symbol:** IOST/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.5813 |
| net_win_rate | 0.4779 |
| gross_profit_factor | 0.9354 |
| gross_win_rate | 0.4779 |
| sharpe_ratio | -3.7721 |
| sortino_ratio | -1.1546 |
| max_drawdown | 0.7386 |
| cagr | -0.4116 |
| net_avg_win | 47.3109 |
| net_avg_loss | -74.4907 |
| avg_hold_time_bars | 5.0442 |
| exposure | 0.1036 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
