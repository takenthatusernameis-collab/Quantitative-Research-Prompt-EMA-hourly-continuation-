# EMA Hourly Continuation — RUNE/USDT P20_34

**Symbol:** RUNE/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.6923 |
| net_win_rate | 0.4954 |
| gross_profit_factor | 1.0081 |
| gross_win_rate | 0.4954 |
| sharpe_ratio | -2.2903 |
| sortino_ratio | -0.5966 |
| max_drawdown | 0.5314 |
| cagr | -0.2393 |
| net_avg_win | 68.5903 |
| net_avg_loss | -97.2793 |
| avg_hold_time_bars | 4.6809 |
| exposure | 0.0700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
