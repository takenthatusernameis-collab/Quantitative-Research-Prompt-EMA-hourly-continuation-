# EMA Hourly Continuation — AXS/USDT P12_50

**Symbol:** AXS/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 595 |
| net_profit_factor | 0.8445 |
| net_win_rate | 0.5261 |
| gross_profit_factor | 1.1127 |
| gross_win_rate | 0.5261 |
| sharpe_ratio | -1.3247 |
| sortino_ratio | -0.4651 |
| max_drawdown | 0.4476 |
| cagr | -0.1938 |
| net_avg_win | 72.7539 |
| net_avg_loss | -95.6216 |
| avg_hold_time_bars | 11.6689 |
| exposure | 0.3142 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
