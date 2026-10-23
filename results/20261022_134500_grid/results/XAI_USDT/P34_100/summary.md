# EMA Hourly Continuation — XAI/USDT P34_100

**Symbol:** XAI/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.6658 |
| net_win_rate | 0.4593 |
| gross_profit_factor | 0.9602 |
| gross_win_rate | 0.4695 |
| sharpe_ratio | -4.4185 |
| sortino_ratio | -1.6365 |
| max_drawdown | 0.8798 |
| cagr | -0.5391 |
| net_avg_win | 54.0358 |
| net_avg_loss | -68.9392 |
| avg_hold_time_bars | 10.0974 |
| exposure | 0.3158 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
