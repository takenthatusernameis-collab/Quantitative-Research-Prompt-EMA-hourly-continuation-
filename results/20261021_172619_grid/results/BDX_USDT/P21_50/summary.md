# EMA Hourly Continuation — BDX/USDT P21_50

**Symbol:** BDX/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.4257 |
| net_win_rate | 0.4092 |
| gross_profit_factor | 0.7068 |
| gross_win_rate | 0.4092 |
| sharpe_ratio | -4.6634 |
| sortino_ratio | -1.1632 |
| max_drawdown | 0.7569 |
| cagr | -0.4208 |
| net_avg_win | 44.6062 |
| net_avg_loss | -72.5898 |
| avg_hold_time_bars | 9.1452 |
| exposure | 0.1260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
