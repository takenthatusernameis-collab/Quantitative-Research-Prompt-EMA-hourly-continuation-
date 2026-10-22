# EMA Hourly Continuation — TRAC/USDT P55_100

**Symbol:** TRAC/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 609 |
| net_profit_factor | 0.6002 |
| net_win_rate | 0.4992 |
| gross_profit_factor | 1.0509 |
| gross_win_rate | 0.5107 |
| sharpe_ratio | -3.9324 |
| sortino_ratio | -1.3665 |
| max_drawdown | 0.8180 |
| cagr | -0.4830 |
| net_avg_win | 39.9680 |
| net_avg_loss | -66.3698 |
| avg_hold_time_bars | 4.8966 |
| exposure | 0.1355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
