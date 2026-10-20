# EMA Hourly Continuation — CSPR/USDT P55_100

**Symbol:** CSPR/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 888 |
| net_profit_factor | 0.3765 |
| net_win_rate | 0.3986 |
| gross_profit_factor | 0.6966 |
| gross_win_rate | 0.4032 |
| sharpe_ratio | -8.8279 |
| sortino_ratio | -3.7307 |
| max_drawdown | 0.9905 |
| cagr | -0.8423 |
| net_avg_win | 16.8953 |
| net_avg_loss | -29.7457 |
| avg_hold_time_bars | 4.0788 |
| exposure | 0.1646 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
