# EMA Hourly Continuation — ETH/USDT P20_34

**Symbol:** ETH/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 251 |
| net_profit_factor | 0.5848 |
| net_win_rate | 0.4940 |
| gross_profit_factor | 0.9850 |
| gross_win_rate | 0.4940 |
| sharpe_ratio | -2.6691 |
| sortino_ratio | -0.6089 |
| max_drawdown | 0.5108 |
| cagr | -0.2423 |
| net_avg_win | 57.0155 |
| net_avg_loss | -95.1865 |
| avg_hold_time_bars | 5.5219 |
| exposure | 0.0630 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
