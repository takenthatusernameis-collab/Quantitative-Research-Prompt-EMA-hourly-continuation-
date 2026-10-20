# EMA Hourly Continuation — AVA/USDT P34_100

**Symbol:** AVA/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 667 |
| net_profit_factor | 0.6032 |
| net_win_rate | 0.5052 |
| gross_profit_factor | 0.9910 |
| gross_win_rate | 0.5082 |
| sharpe_ratio | -3.6776 |
| sortino_ratio | -1.3314 |
| max_drawdown | 0.8139 |
| cagr | -0.4793 |
| net_avg_win | 36.3442 |
| net_avg_loss | -61.5327 |
| avg_hold_time_bars | 8.4078 |
| exposure | 0.2549 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
