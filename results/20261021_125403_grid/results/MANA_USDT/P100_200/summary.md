# EMA Hourly Continuation — MANA/USDT P100_200

**Symbol:** MANA/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.7638 |
| net_win_rate | 0.5033 |
| gross_profit_factor | 1.0031 |
| gross_win_rate | 0.5033 |
| sharpe_ratio | -1.4327 |
| sortino_ratio | -0.3596 |
| max_drawdown | 0.3634 |
| cagr | -0.1525 |
| net_avg_win | 71.4005 |
| net_avg_loss | -94.7124 |
| avg_hold_time_bars | 11.3497 |
| exposure | 0.1579 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
