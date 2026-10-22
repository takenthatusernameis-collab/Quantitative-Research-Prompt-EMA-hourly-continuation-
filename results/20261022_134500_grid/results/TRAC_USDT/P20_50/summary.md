# EMA Hourly Continuation — TRAC/USDT P20_50

**Symbol:** TRAC/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 833 |
| net_profit_factor | 0.5374 |
| net_win_rate | 0.4778 |
| gross_profit_factor | 0.9322 |
| gross_win_rate | 0.4886 |
| sharpe_ratio | -5.4082 |
| sortino_ratio | -2.1932 |
| max_drawdown | 0.9355 |
| cagr | -0.6552 |
| net_avg_win | 27.1749 |
| net_avg_loss | -46.2663 |
| avg_hold_time_bars | 6.4250 |
| exposure | 0.2433 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
