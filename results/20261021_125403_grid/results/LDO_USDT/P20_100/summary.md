# EMA Hourly Continuation — LDO/USDT P20_100

**Symbol:** LDO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.7172 |
| net_win_rate | 0.4637 |
| gross_profit_factor | 0.8606 |
| gross_win_rate | 0.4637 |
| sharpe_ratio | -2.2673 |
| sortino_ratio | -0.6862 |
| max_drawdown | 0.5642 |
| cagr | -0.2712 |
| net_avg_win | 65.8840 |
| net_avg_loss | -79.4379 |
| avg_hold_time_bars | 20.0044 |
| exposure | 0.4137 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
