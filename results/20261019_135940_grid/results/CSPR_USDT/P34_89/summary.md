# EMA Hourly Continuation — CSPR/USDT P34_89

**Symbol:** CSPR/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 983 |
| net_profit_factor | 0.4529 |
| net_win_rate | 0.4201 |
| gross_profit_factor | 0.8058 |
| gross_win_rate | 0.4283 |
| sharpe_ratio | -7.7563 |
| sortino_ratio | -3.4407 |
| max_drawdown | 0.9854 |
| cagr | -0.8109 |
| net_avg_win | 19.7420 |
| net_avg_loss | -31.5804 |
| avg_hold_time_bars | 5.4486 |
| exposure | 0.2435 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
