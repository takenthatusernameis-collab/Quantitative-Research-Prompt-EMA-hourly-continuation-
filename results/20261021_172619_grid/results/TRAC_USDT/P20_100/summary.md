# EMA Hourly Continuation — TRAC/USDT P20_100

**Symbol:** TRAC/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 503 |
| net_profit_factor | 0.8646 |
| net_win_rate | 0.5169 |
| gross_profit_factor | 1.0719 |
| gross_win_rate | 0.5169 |
| sharpe_ratio | -1.0239 |
| sortino_ratio | -0.3302 |
| max_drawdown | 0.3588 |
| cagr | -0.1436 |
| net_avg_win | 79.2408 |
| net_avg_loss | -98.0571 |
| avg_hold_time_bars | 15.2604 |
| exposure | 0.3489 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
