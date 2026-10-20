# EMA Hourly Continuation — DIA/USDT P20_50

**Symbol:** DIA/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 973 |
| net_profit_factor | 0.4473 |
| net_win_rate | 0.4337 |
| gross_profit_factor | 0.8037 |
| gross_win_rate | 0.4512 |
| sharpe_ratio | -7.5393 |
| sortino_ratio | -3.2936 |
| max_drawdown | 0.9834 |
| cagr | -0.8019 |
| net_avg_win | 18.8564 |
| net_avg_loss | -32.2848 |
| avg_hold_time_bars | 5.2518 |
| exposure | 0.2312 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
