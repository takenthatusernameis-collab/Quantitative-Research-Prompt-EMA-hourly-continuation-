# EMA Hourly Continuation — STRK/USDT P8_34

**Symbol:** STRK/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1431 |
| net_profit_factor | 0.5114 |
| net_win_rate | 0.4507 |
| gross_profit_factor | 0.8781 |
| gross_win_rate | 0.4612 |
| sharpe_ratio | -7.9528 |
| sortino_ratio | -4.2187 |
| max_drawdown | 0.9945 |
| cagr | -0.8719 |
| net_avg_win | 16.1323 |
| net_avg_loss | -25.8880 |
| avg_hold_time_bars | 4.9532 |
| exposure | 0.3222 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
