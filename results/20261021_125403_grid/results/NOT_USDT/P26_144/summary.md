# EMA Hourly Continuation — NOT/USDT P26_144

**Symbol:** NOT/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.8442 |
| net_win_rate | 0.4985 |
| gross_profit_factor | 1.0054 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -1.0435 |
| sortino_ratio | -0.2763 |
| max_drawdown | 0.3581 |
| cagr | -0.1209 |
| net_avg_win | 88.2842 |
| net_avg_loss | -103.9504 |
| avg_hold_time_bars | 30.9305 |
| exposure | 0.4809 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
