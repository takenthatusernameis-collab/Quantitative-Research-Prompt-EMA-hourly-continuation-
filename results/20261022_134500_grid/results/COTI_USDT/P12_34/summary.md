# EMA Hourly Continuation — COTI/USDT P12_34

**Symbol:** COTI/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1360 |
| net_profit_factor | 0.4790 |
| net_win_rate | 0.4390 |
| gross_profit_factor | 0.8323 |
| gross_win_rate | 0.4463 |
| sharpe_ratio | -8.8391 |
| sortino_ratio | -4.5730 |
| max_drawdown | 0.9966 |
| cagr | -0.8954 |
| net_avg_win | 15.3465 |
| net_avg_loss | -25.0686 |
| avg_hold_time_bars | 3.6037 |
| exposure | 0.2228 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
