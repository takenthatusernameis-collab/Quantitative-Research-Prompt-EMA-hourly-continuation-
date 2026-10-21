# EMA Hourly Continuation — ZRO/USDT P8_21

**Symbol:** ZRO/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.9442 |
| net_win_rate | 0.5463 |
| gross_profit_factor | 1.1960 |
| gross_win_rate | 0.5463 |
| sharpe_ratio | -0.3607 |
| sortino_ratio | -0.1157 |
| max_drawdown | 0.3309 |
| cagr | -0.0583 |
| net_avg_win | 89.2376 |
| net_avg_loss | -113.7818 |
| avg_hold_time_bars | 6.0771 |
| exposure | 0.1350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
