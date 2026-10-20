# EMA Hourly Continuation — ETN/USDT P144_200

**Symbol:** ETN/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.3809 |
| net_win_rate | 0.3593 |
| gross_profit_factor | 0.6470 |
| gross_win_rate | 0.3776 |
| sharpe_ratio | -7.8685 |
| sortino_ratio | -2.5486 |
| max_drawdown | 0.9331 |
| cagr | -0.7227 |
| net_avg_win | 36.5490 |
| net_avg_loss | -53.7964 |
| avg_hold_time_bars | 5.0961 |
| exposure | 0.1210 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
