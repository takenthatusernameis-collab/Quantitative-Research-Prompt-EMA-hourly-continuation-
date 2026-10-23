# EMA Hourly Continuation — PHA/USDT P8_89

**Symbol:** PHA/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 796 |
| net_profit_factor | 0.6136 |
| net_win_rate | 0.4598 |
| gross_profit_factor | 0.8889 |
| gross_win_rate | 0.4623 |
| sharpe_ratio | -4.4558 |
| sortino_ratio | -1.7591 |
| max_drawdown | 0.8828 |
| cagr | -0.5717 |
| net_avg_win | 38.2239 |
| net_avg_loss | -53.0257 |
| avg_hold_time_bars | 16.6796 |
| exposure | 0.6035 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
