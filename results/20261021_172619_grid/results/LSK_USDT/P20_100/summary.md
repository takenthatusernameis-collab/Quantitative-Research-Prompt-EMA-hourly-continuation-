# EMA Hourly Continuation — LSK/USDT P20_100

**Symbol:** LSK/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.7321 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 0.9559 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -2.2216 |
| sortino_ratio | -0.7006 |
| max_drawdown | 0.5901 |
| cagr | -0.2772 |
| net_avg_win | 64.2912 |
| net_avg_loss | -82.5870 |
| avg_hold_time_bars | 18.8773 |
| exposure | 0.4196 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
