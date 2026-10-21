# EMA Hourly Continuation — TAIKO/USDT P26_34

**Symbol:** TAIKO/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 210 |
| net_profit_factor | 0.6750 |
| net_win_rate | 0.5143 |
| gross_profit_factor | 1.0487 |
| gross_win_rate | 0.5143 |
| sharpe_ratio | -1.7954 |
| sortino_ratio | -0.3836 |
| max_drawdown | 0.3810 |
| cagr | -0.1612 |
| net_avg_win | 65.6633 |
| net_avg_loss | -103.0088 |
| avg_hold_time_bars | 6.1810 |
| exposure | 0.0623 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
