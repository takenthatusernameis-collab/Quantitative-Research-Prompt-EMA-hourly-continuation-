# EMA Hourly Continuation — GALA/USDT P20_144

**Symbol:** GALA/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.6309 |
| net_win_rate | 0.4644 |
| gross_profit_factor | 0.8790 |
| gross_win_rate | 0.4690 |
| sharpe_ratio | -2.9806 |
| sortino_ratio | -0.8750 |
| max_drawdown | 0.6511 |
| cagr | -0.3401 |
| net_avg_win | 54.8140 |
| net_avg_loss | -75.3276 |
| avg_hold_time_bars | 29.2920 |
| exposure | 0.5792 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
