# EMA Hourly Continuation — DOT/USDT P21_89

**Symbol:** DOT/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.8245 |
| net_win_rate | 0.5134 |
| gross_profit_factor | 1.0481 |
| gross_win_rate | 0.5134 |
| sharpe_ratio | -1.2516 |
| sortino_ratio | -0.3809 |
| max_drawdown | 0.4290 |
| cagr | -0.1619 |
| net_avg_win | 73.1730 |
| net_avg_loss | -93.6333 |
| avg_hold_time_bars | 18.4821 |
| exposure | 0.3764 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
