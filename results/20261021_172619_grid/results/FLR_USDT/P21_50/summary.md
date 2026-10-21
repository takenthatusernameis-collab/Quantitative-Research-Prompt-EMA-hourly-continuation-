# EMA Hourly Continuation — FLR/USDT P21_50

**Symbol:** FLR/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 528 |
| net_profit_factor | 0.5560 |
| net_win_rate | 0.4451 |
| gross_profit_factor | 0.7883 |
| gross_win_rate | 0.4470 |
| sharpe_ratio | -4.2384 |
| sortino_ratio | -1.3901 |
| max_drawdown | 0.8119 |
| cagr | -0.4701 |
| net_avg_win | 42.4753 |
| net_avg_loss | -61.2712 |
| avg_hold_time_bars | 6.9773 |
| exposure | 0.1675 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
