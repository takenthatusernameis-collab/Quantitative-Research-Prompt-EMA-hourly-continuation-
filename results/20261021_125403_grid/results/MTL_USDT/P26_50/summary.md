# EMA Hourly Continuation — MTL/USDT P26_50

**Symbol:** MTL/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.5841 |
| net_win_rate | 0.4552 |
| gross_profit_factor | 0.8930 |
| gross_win_rate | 0.4552 |
| sharpe_ratio | -4.4040 |
| sortino_ratio | -1.4408 |
| max_drawdown | 0.8258 |
| cagr | -0.4879 |
| net_avg_win | 47.8977 |
| net_avg_loss | -68.5266 |
| avg_hold_time_bars | 8.7029 |
| exposure | 0.2068 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
