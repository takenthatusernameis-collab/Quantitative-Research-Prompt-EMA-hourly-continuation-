# EMA Hourly Continuation — MINA/USDT P20_50

**Symbol:** MINA/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 981 |
| net_profit_factor | 0.5876 |
| net_win_rate | 0.4811 |
| gross_profit_factor | 1.0514 |
| gross_win_rate | 0.4995 |
| sharpe_ratio | -5.7268 |
| sortino_ratio | -2.5373 |
| max_drawdown | 0.9553 |
| cagr | -0.7030 |
| net_avg_win | 28.7604 |
| net_avg_loss | -45.3846 |
| avg_hold_time_bars | 5.8257 |
| exposure | 0.2598 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
