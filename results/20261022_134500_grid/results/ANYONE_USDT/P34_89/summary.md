# EMA Hourly Continuation — ANYONE/USDT P34_89

**Symbol:** ANYONE/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 590 |
| net_profit_factor | 0.5634 |
| net_win_rate | 0.4288 |
| gross_profit_factor | 0.7592 |
| gross_win_rate | 0.4339 |
| sharpe_ratio | -4.7344 |
| sortino_ratio | -1.7069 |
| max_drawdown | 0.8410 |
| cagr | -0.5535 |
| net_avg_win | 42.7603 |
| net_avg_loss | -56.9754 |
| avg_hold_time_bars | 7.5881 |
| exposure | 0.2262 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
