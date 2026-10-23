# EMA Hourly Continuation — AVA/USDT P21_50

**Symbol:** AVA/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 970 |
| net_profit_factor | 0.4352 |
| net_win_rate | 0.4536 |
| gross_profit_factor | 0.8344 |
| gross_win_rate | 0.4701 |
| sharpe_ratio | -7.5628 |
| sortino_ratio | -3.3044 |
| max_drawdown | 0.9847 |
| cagr | -0.8081 |
| net_avg_win | 17.2354 |
| net_avg_loss | -32.8778 |
| avg_hold_time_bars | 4.3753 |
| exposure | 0.1929 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
