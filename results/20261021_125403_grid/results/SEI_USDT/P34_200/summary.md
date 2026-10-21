# EMA Hourly Continuation — SEI/USDT P34_200

**Symbol:** SEI/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 261 |
| net_profit_factor | 0.8834 |
| net_win_rate | 0.5134 |
| gross_profit_factor | 1.0377 |
| gross_win_rate | 0.5134 |
| sharpe_ratio | -0.5733 |
| sortino_ratio | -0.1328 |
| max_drawdown | 0.2106 |
| cagr | -0.0615 |
| net_avg_win | 83.2956 |
| net_avg_loss | -99.4885 |
| avg_hold_time_bars | 44.6667 |
| exposure | 0.5299 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
