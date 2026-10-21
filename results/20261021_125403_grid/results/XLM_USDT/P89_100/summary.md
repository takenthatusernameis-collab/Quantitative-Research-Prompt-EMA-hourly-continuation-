# EMA Hourly Continuation — XLM/USDT P89_100

**Symbol:** XLM/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 81 |
| net_profit_factor | 0.6257 |
| net_win_rate | 0.4938 |
| gross_profit_factor | 0.9631 |
| gross_win_rate | 0.4938 |
| sharpe_ratio | -1.2565 |
| sortino_ratio | -0.1630 |
| max_drawdown | 0.1836 |
| cagr | -0.0714 |
| net_avg_win | 70.9256 |
| net_avg_loss | -110.5958 |
| avg_hold_time_bars | 6.4444 |
| exposure | 0.0237 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
