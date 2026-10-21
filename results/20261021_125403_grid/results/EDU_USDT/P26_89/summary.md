# EMA Hourly Continuation — EDU/USDT P26_89

**Symbol:** EDU/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 569 |
| net_profit_factor | 0.7591 |
| net_win_rate | 0.4938 |
| gross_profit_factor | 0.9616 |
| gross_win_rate | 0.4938 |
| sharpe_ratio | -1.9798 |
| sortino_ratio | -0.6739 |
| max_drawdown | 0.5657 |
| cagr | -0.2672 |
| net_avg_win | 60.9413 |
| net_avg_loss | -78.3325 |
| avg_hold_time_bars | 11.3708 |
| exposure | 0.2928 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
