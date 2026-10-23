# EMA Hourly Continuation — TAIKO/USDT P21_34

**Symbol:** TAIKO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1012 |
| net_profit_factor | 0.4152 |
| net_win_rate | 0.4190 |
| gross_profit_factor | 0.8614 |
| gross_win_rate | 0.4536 |
| sharpe_ratio | -10.5266 |
| sortino_ratio | -4.8794 |
| max_drawdown | 0.9974 |
| cagr | -0.9180 |
| net_avg_win | 16.6989 |
| net_avg_loss | -29.0036 |
| avg_hold_time_bars | 3.1275 |
| exposure | 0.1520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
