# EMA Hourly Continuation — UMA/USDT P12_21

**Symbol:** UMA/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1343 |
| net_profit_factor | 0.3207 |
| net_win_rate | 0.3976 |
| gross_profit_factor | 0.7776 |
| gross_win_rate | 0.4319 |
| sharpe_ratio | -12.3851 |
| sortino_ratio | -6.4885 |
| max_drawdown | 0.9997 |
| cagr | -0.9626 |
| net_avg_win | 8.8400 |
| net_avg_loss | -18.1928 |
| avg_hold_time_bars | 2.8198 |
| exposure | 0.1721 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
