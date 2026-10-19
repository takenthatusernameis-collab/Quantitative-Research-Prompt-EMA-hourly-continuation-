# EMA Hourly Continuation — KAS/USDT P12_34

**Symbol:** KAS/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1361 |
| net_profit_factor | 0.4140 |
| net_win_rate | 0.4614 |
| gross_profit_factor | 0.8611 |
| gross_win_rate | 0.4820 |
| sharpe_ratio | -8.7523 |
| sortino_ratio | -4.5286 |
| max_drawdown | 0.9966 |
| cagr | -0.8957 |
| net_avg_win | 11.2096 |
| net_avg_loss | -23.1997 |
| avg_hold_time_bars | 3.8736 |
| exposure | 0.2396 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
