# EMA Hourly Continuation — GRT/USDT P100_200

**Symbol:** GRT/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.5370 |
| net_win_rate | 0.4828 |
| gross_profit_factor | 0.9142 |
| gross_win_rate | 0.4855 |
| sharpe_ratio | -3.7294 |
| sortino_ratio | -1.0099 |
| max_drawdown | 0.7462 |
| cagr | -0.3974 |
| net_avg_win | 45.7057 |
| net_avg_loss | -79.4748 |
| avg_hold_time_bars | 8.6412 |
| exposure | 0.1482 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
