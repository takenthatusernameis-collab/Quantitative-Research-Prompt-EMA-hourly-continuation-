# EMA Hourly Continuation — COTI/USDT P26_50

**Symbol:** COTI/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1012 |
| net_profit_factor | 0.5077 |
| net_win_rate | 0.4358 |
| gross_profit_factor | 0.8803 |
| gross_win_rate | 0.4476 |
| sharpe_ratio | -7.7822 |
| sortino_ratio | -3.5076 |
| max_drawdown | 0.9869 |
| cagr | -0.8167 |
| net_avg_win | 23.0593 |
| net_avg_loss | -35.0754 |
| avg_hold_time_bars | 3.3834 |
| exposure | 0.1556 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
