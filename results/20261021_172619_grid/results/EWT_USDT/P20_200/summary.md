# EMA Hourly Continuation — EWT/USDT P20_200

**Symbol:** EWT/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.7594 |
| net_win_rate | 0.4742 |
| gross_profit_factor | 0.8911 |
| gross_win_rate | 0.4742 |
| sharpe_ratio | -1.6726 |
| sortino_ratio | -0.4679 |
| max_drawdown | 0.5185 |
| cagr | -0.1948 |
| net_avg_win | 71.9886 |
| net_avg_loss | -85.5040 |
| avg_hold_time_bars | 28.4639 |
| exposure | 0.5020 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
