# EMA Hourly Continuation — AR/USDT P20_100

**Symbol:** AR/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 650 |
| net_profit_factor | 0.6361 |
| net_win_rate | 0.4677 |
| gross_profit_factor | 0.9040 |
| gross_win_rate | 0.4754 |
| sharpe_ratio | -3.7562 |
| sortino_ratio | -1.3399 |
| max_drawdown | 0.8114 |
| cagr | -0.4762 |
| net_avg_win | 46.1639 |
| net_avg_loss | -63.7635 |
| avg_hold_time_bars | 14.2846 |
| exposure | 0.4220 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
