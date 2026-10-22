# EMA Hourly Continuation — ORBS/USDT P20_144

**Symbol:** ORBS/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.7402 |
| net_win_rate | 0.4812 |
| gross_profit_factor | 0.9593 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -2.1573 |
| sortino_ratio | -0.6137 |
| max_drawdown | 0.5814 |
| cagr | -0.2459 |
| net_avg_win | 75.3441 |
| net_avg_loss | -94.4157 |
| avg_hold_time_bars | 32.2682 |
| exposure | 0.5852 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
