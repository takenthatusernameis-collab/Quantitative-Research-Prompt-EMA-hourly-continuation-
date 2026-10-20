# EMA Hourly Continuation — XAI/USDT P8_50

**Symbol:** XAI/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1158 |
| net_profit_factor | 0.6898 |
| net_win_rate | 0.4491 |
| gross_profit_factor | 0.9909 |
| gross_win_rate | 0.4629 |
| sharpe_ratio | -6.3578 |
| sortino_ratio | -3.0424 |
| max_drawdown | 0.9773 |
| cagr | -0.7669 |
| net_avg_win | 41.6627 |
| net_avg_loss | -49.2267 |
| avg_hold_time_bars | 9.0691 |
| exposure | 0.4774 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
