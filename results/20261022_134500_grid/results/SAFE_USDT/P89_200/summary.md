# EMA Hourly Continuation — SAFE/USDT P89_200

**Symbol:** SAFE/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.5624 |
| net_win_rate | 0.4536 |
| gross_profit_factor | 0.8262 |
| gross_win_rate | 0.4536 |
| sharpe_ratio | -3.4139 |
| sortino_ratio | -0.9413 |
| max_drawdown | 0.6722 |
| cagr | -0.3583 |
| net_avg_win | 50.2763 |
| net_avg_loss | -74.2104 |
| avg_hold_time_bars | 12.0743 |
| exposure | 0.2085 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
