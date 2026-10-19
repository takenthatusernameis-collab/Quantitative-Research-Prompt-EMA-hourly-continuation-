# EMA Hourly Continuation — XMR/USDT P12_50

**Symbol:** XMR/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1401 |
| net_profit_factor | 0.2729 |
| net_win_rate | 0.4083 |
| gross_profit_factor | 0.6245 |
| gross_win_rate | 0.4211 |
| sharpe_ratio | -11.7042 |
| sortino_ratio | -6.1516 |
| max_drawdown | 0.9997 |
| cagr | -0.9582 |
| net_avg_win | 6.5594 |
| net_avg_loss | -16.5845 |
| avg_hold_time_bars | 5.0214 |
| exposure | 0.3198 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
