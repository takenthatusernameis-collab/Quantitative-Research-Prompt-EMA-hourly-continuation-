# EMA Hourly Continuation — MTL/USDT P20_50

**Symbol:** MTL/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 582 |
| net_profit_factor | 0.6895 |
| net_win_rate | 0.4931 |
| gross_profit_factor | 1.0173 |
| gross_win_rate | 0.4931 |
| sharpe_ratio | -3.2535 |
| sortino_ratio | -1.1223 |
| max_drawdown | 0.7475 |
| cagr | -0.4044 |
| net_avg_win | 56.4392 |
| net_avg_loss | -79.6323 |
| avg_hold_time_bars | 9.8952 |
| exposure | 0.2606 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
