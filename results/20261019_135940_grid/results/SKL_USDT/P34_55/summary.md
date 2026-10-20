# EMA Hourly Continuation — SKL/USDT P34_55

**Symbol:** SKL/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 921 |
| net_profit_factor | 0.4514 |
| net_win_rate | 0.4549 |
| gross_profit_factor | 0.9023 |
| gross_win_rate | 0.4777 |
| sharpe_ratio | -7.4938 |
| sortino_ratio | -3.2285 |
| max_drawdown | 0.9808 |
| cagr | -0.7907 |
| net_avg_win | 19.2488 |
| net_avg_loss | -35.5942 |
| avg_hold_time_bars | 3.3561 |
| exposure | 0.1405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
