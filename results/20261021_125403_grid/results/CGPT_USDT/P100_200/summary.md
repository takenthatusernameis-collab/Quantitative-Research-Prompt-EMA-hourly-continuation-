# EMA Hourly Continuation — CGPT/USDT P100_200

**Symbol:** CGPT/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 248 |
| net_profit_factor | 0.8277 |
| net_win_rate | 0.5081 |
| gross_profit_factor | 1.0378 |
| gross_win_rate | 0.5121 |
| sharpe_ratio | -0.9269 |
| sortino_ratio | -0.2094 |
| max_drawdown | 0.2788 |
| cagr | -0.0928 |
| net_avg_win | 82.7104 |
| net_avg_loss | -103.2005 |
| avg_hold_time_bars | 10.9879 |
| exposure | 0.1239 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
