# EMA Hourly Continuation — DAG/USDT P34_89

**Symbol:** DAG/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 725 |
| net_profit_factor | 0.4842 |
| net_win_rate | 0.4234 |
| gross_profit_factor | 0.7604 |
| gross_win_rate | 0.4317 |
| sharpe_ratio | -6.3706 |
| sortino_ratio | -2.3911 |
| max_drawdown | 0.9516 |
| cagr | -0.6976 |
| net_avg_win | 29.0592 |
| net_avg_loss | -44.0792 |
| avg_hold_time_bars | 6.3283 |
| exposure | 0.2085 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
