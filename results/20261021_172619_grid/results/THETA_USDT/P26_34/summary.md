# EMA Hourly Continuation — THETA/USDT P26_34

**Symbol:** THETA/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 171 |
| net_profit_factor | 0.6583 |
| net_win_rate | 0.4795 |
| gross_profit_factor | 0.9238 |
| gross_win_rate | 0.4795 |
| sharpe_ratio | -1.7133 |
| sortino_ratio | -0.3214 |
| max_drawdown | 0.3272 |
| cagr | -0.1366 |
| net_avg_win | 72.4729 |
| net_avg_loss | -101.4331 |
| avg_hold_time_bars | 5.2515 |
| exposure | 0.0408 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
