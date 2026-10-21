# EMA Hourly Continuation — ADA/USDT P34_50

**Symbol:** ADA/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 217 |
| net_profit_factor | 0.6297 |
| net_win_rate | 0.4793 |
| gross_profit_factor | 0.9266 |
| gross_win_rate | 0.4793 |
| sharpe_ratio | -2.0940 |
| sortino_ratio | -0.4423 |
| max_drawdown | 0.3978 |
| cagr | -0.1829 |
| net_avg_win | 65.0530 |
| net_avg_loss | -95.0784 |
| avg_hold_time_bars | 5.0829 |
| exposure | 0.0501 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
