# EMA Hourly Continuation — ZRO/USDT P20_21

**Symbol:** ZRO/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 107 |
| net_profit_factor | 0.8464 |
| net_win_rate | 0.5234 |
| gross_profit_factor | 1.0885 |
| gross_win_rate | 0.5234 |
| sharpe_ratio | -0.5346 |
| sortino_ratio | -0.0827 |
| max_drawdown | 0.1570 |
| cagr | -0.0380 |
| net_avg_win | 84.9756 |
| net_avg_loss | -110.2372 |
| avg_hold_time_bars | 4.3551 |
| exposure | 0.0228 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
