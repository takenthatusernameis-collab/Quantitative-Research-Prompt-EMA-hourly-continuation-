# EMA Hourly Continuation — ANYONE/USDT P8_20

**Symbol:** ANYONE/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 540 |
| net_profit_factor | 0.7254 |
| net_win_rate | 0.4778 |
| gross_profit_factor | 0.9130 |
| gross_win_rate | 0.4778 |
| sharpe_ratio | -2.6009 |
| sortino_ratio | -0.9079 |
| max_drawdown | 0.6403 |
| cagr | -0.3426 |
| net_avg_win | 62.6968 |
| net_avg_loss | -79.0727 |
| avg_hold_time_bars | 6.0833 |
| exposure | 0.1660 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
