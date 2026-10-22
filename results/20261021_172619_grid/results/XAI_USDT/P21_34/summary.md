# EMA Hourly Continuation — XAI/USDT P21_34

**Symbol:** XAI/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.6461 |
| net_win_rate | 0.4562 |
| gross_profit_factor | 0.8665 |
| gross_win_rate | 0.4562 |
| sharpe_ratio | -3.0064 |
| sortino_ratio | -0.8440 |
| max_drawdown | 0.6489 |
| cagr | -0.3208 |
| net_avg_win | 64.0978 |
| net_avg_loss | -83.2236 |
| avg_hold_time_bars | 4.9768 |
| exposure | 0.0878 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
