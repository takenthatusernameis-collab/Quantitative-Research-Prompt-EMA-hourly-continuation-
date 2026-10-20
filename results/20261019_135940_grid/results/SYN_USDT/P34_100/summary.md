# EMA Hourly Continuation — SYN/USDT P34_100

**Symbol:** SYN/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 643 |
| net_profit_factor | 0.6558 |
| net_win_rate | 0.4806 |
| gross_profit_factor | 0.9835 |
| gross_win_rate | 0.4837 |
| sharpe_ratio | -3.7012 |
| sortino_ratio | -1.3124 |
| max_drawdown | 0.8033 |
| cagr | -0.4731 |
| net_avg_win | 49.3282 |
| net_avg_loss | -69.5872 |
| avg_hold_time_bars | 10.3686 |
| exposure | 0.3030 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
