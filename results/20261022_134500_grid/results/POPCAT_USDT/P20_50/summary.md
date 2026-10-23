# EMA Hourly Continuation — POPCAT/USDT P20_50

**Symbol:** POPCAT/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 870 |
| net_profit_factor | 0.5399 |
| net_win_rate | 0.4207 |
| gross_profit_factor | 0.7961 |
| gross_win_rate | 0.4287 |
| sharpe_ratio | -7.3969 |
| sortino_ratio | -3.2984 |
| max_drawdown | 0.9696 |
| cagr | -0.8008 |
| net_avg_win | 31.0822 |
| net_avg_loss | -41.8054 |
| avg_hold_time_bars | 4.8023 |
| exposure | 0.2207 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
