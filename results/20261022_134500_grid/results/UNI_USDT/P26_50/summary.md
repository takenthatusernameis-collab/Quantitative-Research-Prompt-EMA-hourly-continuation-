# EMA Hourly Continuation — UNI/USDT P26_50

**Symbol:** UNI/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 976 |
| net_profit_factor | 0.4035 |
| net_win_rate | 0.4293 |
| gross_profit_factor | 0.7816 |
| gross_win_rate | 0.4426 |
| sharpe_ratio | -8.5290 |
| sortino_ratio | -3.7504 |
| max_drawdown | 0.9913 |
| cagr | -0.8471 |
| net_avg_win | 16.0010 |
| net_avg_loss | -29.8293 |
| avg_hold_time_bars | 3.5287 |
| exposure | 0.1565 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
