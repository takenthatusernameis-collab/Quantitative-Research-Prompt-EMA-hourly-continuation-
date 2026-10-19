# EMA Hourly Continuation — UNI/USDT P21_26

**Symbol:** UNI/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1181 |
| net_profit_factor | 0.1931 |
| net_win_rate | 0.3489 |
| gross_profit_factor | 0.6453 |
| gross_win_rate | 0.3946 |
| sharpe_ratio | -14.9433 |
| sortino_ratio | -7.5356 |
| max_drawdown | 1.0000 |
| cagr | -0.9823 |
| net_avg_win | 5.8074 |
| net_avg_loss | -16.1148 |
| avg_hold_time_bars | 1.6850 |
| exposure | 0.0905 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
