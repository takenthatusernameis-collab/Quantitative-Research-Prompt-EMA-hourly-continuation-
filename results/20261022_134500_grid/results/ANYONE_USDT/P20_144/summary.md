# EMA Hourly Continuation — ANYONE/USDT P20_144

**Symbol:** ANYONE/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.7347 |
| net_win_rate | 0.4850 |
| gross_profit_factor | 0.9343 |
| gross_win_rate | 0.4875 |
| sharpe_ratio | -1.9482 |
| sortino_ratio | -0.5753 |
| max_drawdown | 0.4879 |
| cagr | -0.2419 |
| net_avg_win | 66.3819 |
| net_avg_loss | -85.0945 |
| avg_hold_time_bars | 26.9125 |
| exposure | 0.5440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
