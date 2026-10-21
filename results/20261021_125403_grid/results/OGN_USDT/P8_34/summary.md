# EMA Hourly Continuation — OGN/USDT P8_34

**Symbol:** OGN/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 802 |
| net_profit_factor | 0.6455 |
| net_win_rate | 0.4663 |
| gross_profit_factor | 0.8880 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -4.1668 |
| sortino_ratio | -1.6791 |
| max_drawdown | 0.8613 |
| cagr | -0.5383 |
| net_avg_win | 41.7619 |
| net_avg_loss | -56.5320 |
| avg_hold_time_bars | 8.5736 |
| exposure | 0.3111 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
