# EMA Hourly Continuation — SLP/USDT P20_50

**Symbol:** SLP/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1146 |
| net_profit_factor | 0.4889 |
| net_win_rate | 0.4084 |
| gross_profit_factor | 0.8436 |
| gross_win_rate | 0.4197 |
| sharpe_ratio | -9.5608 |
| sortino_ratio | -4.5731 |
| max_drawdown | 0.9968 |
| cagr | -0.8957 |
| net_avg_win | 20.3682 |
| net_avg_loss | -28.7582 |
| avg_hold_time_bars | 4.4913 |
| exposure | 0.2340 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
