# EMA Hourly Continuation — UMA/USDT P26_50

**Symbol:** UMA/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 916 |
| net_profit_factor | 0.4426 |
| net_win_rate | 0.4454 |
| gross_profit_factor | 0.8498 |
| gross_win_rate | 0.4651 |
| sharpe_ratio | -7.4429 |
| sortino_ratio | -3.2082 |
| max_drawdown | 0.9796 |
| cagr | -0.7861 |
| net_avg_win | 19.0568 |
| net_avg_loss | -34.5812 |
| avg_hold_time_bars | 4.7096 |
| exposure | 0.1961 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
