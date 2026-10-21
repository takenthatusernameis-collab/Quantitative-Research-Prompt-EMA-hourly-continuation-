# EMA Hourly Continuation — ORCA/USDT P100_144

**Symbol:** ORCA/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 285 |
| net_profit_factor | 0.6408 |
| net_win_rate | 0.4807 |
| gross_profit_factor | 0.9190 |
| gross_win_rate | 0.4807 |
| sharpe_ratio | -2.3465 |
| sortino_ratio | -0.5644 |
| max_drawdown | 0.5054 |
| cagr | -0.2310 |
| net_avg_win | 62.8915 |
| net_avg_loss | -90.8534 |
| avg_hold_time_bars | 7.0035 |
| exposure | 0.0907 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
