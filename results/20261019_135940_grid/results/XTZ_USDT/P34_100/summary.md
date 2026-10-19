# EMA Hourly Continuation — XTZ/USDT P34_100

**Symbol:** XTZ/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 683 |
| net_profit_factor | 0.5980 |
| net_win_rate | 0.4832 |
| gross_profit_factor | 1.0230 |
| gross_win_rate | 0.5037 |
| sharpe_ratio | -4.3400 |
| sortino_ratio | -1.6105 |
| max_drawdown | 0.8541 |
| cagr | -0.5318 |
| net_avg_win | 38.3734 |
| net_avg_loss | -59.9897 |
| avg_hold_time_bars | 9.2489 |
| exposure | 0.2871 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
