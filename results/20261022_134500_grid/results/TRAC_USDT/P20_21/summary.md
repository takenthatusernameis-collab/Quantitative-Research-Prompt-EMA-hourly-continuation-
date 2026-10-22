# EMA Hourly Continuation — TRAC/USDT P20_21

**Symbol:** TRAC/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 991 |
| net_profit_factor | 0.1628 |
| net_win_rate | 0.2947 |
| gross_profit_factor | 0.6325 |
| gross_win_rate | 0.3734 |
| sharpe_ratio | -15.6068 |
| sortino_ratio | -7.3232 |
| max_drawdown | 1.0000 |
| cagr | -0.9856 |
| net_avg_win | 6.6608 |
| net_avg_loss | -17.0883 |
| avg_hold_time_bars | 2.7871 |
| exposure | 0.1255 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
