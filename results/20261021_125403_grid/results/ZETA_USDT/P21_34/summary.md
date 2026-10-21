# EMA Hourly Continuation — ZETA/USDT P21_34

**Symbol:** ZETA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.6496 |
| net_win_rate | 0.4935 |
| gross_profit_factor | 0.9400 |
| gross_win_rate | 0.4935 |
| sharpe_ratio | -2.4888 |
| sortino_ratio | -0.6982 |
| max_drawdown | 0.5749 |
| cagr | -0.2720 |
| net_avg_win | 54.0458 |
| net_avg_loss | -81.0582 |
| avg_hold_time_bars | 4.9713 |
| exposure | 0.0862 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
