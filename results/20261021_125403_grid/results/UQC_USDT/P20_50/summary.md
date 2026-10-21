# EMA Hourly Continuation — UQC/USDT P20_50

**Symbol:** UQC/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.4236 |
| net_win_rate | 0.3433 |
| gross_profit_factor | 0.6299 |
| gross_win_rate | 0.3507 |
| sharpe_ratio | -4.9111 |
| sortino_ratio | -1.1251 |
| max_drawdown | 0.7475 |
| cagr | -0.4183 |
| net_avg_win | 59.5228 |
| net_avg_loss | -73.4454 |
| avg_hold_time_bars | 42.0896 |
| exposure | 0.5105 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
