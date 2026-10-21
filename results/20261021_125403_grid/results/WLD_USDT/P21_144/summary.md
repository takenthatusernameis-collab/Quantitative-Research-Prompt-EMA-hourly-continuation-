# EMA Hourly Continuation — WLD/USDT P21_144

**Symbol:** WLD/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 332 |
| net_profit_factor | 1.0820 |
| net_win_rate | 0.5542 |
| gross_profit_factor | 1.2301 |
| gross_win_rate | 0.5542 |
| sharpe_ratio | 0.5116 |
| sortino_ratio | 0.1357 |
| max_drawdown | 0.1197 |
| cagr | 0.0535 |
| net_avg_win | 100.3298 |
| net_avg_loss | -115.2834 |
| avg_hold_time_bars | 36.2530 |
| exposure | 0.5471 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
