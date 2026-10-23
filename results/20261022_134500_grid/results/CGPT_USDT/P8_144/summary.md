# EMA Hourly Continuation — CGPT/USDT P8_144

**Symbol:** CGPT/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.7223 |
| net_win_rate | 0.4968 |
| gross_profit_factor | 0.9932 |
| gross_win_rate | 0.5053 |
| sharpe_ratio | -2.0669 |
| sortino_ratio | -0.6334 |
| max_drawdown | 0.5523 |
| cagr | -0.2612 |
| net_avg_win | 58.9345 |
| net_avg_loss | -80.5647 |
| avg_hold_time_bars | 35.2791 |
| exposure | 0.7585 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
