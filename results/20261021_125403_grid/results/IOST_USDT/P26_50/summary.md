# EMA Hourly Continuation — IOST/USDT P26_50

**Symbol:** IOST/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.6454 |
| net_win_rate | 0.4990 |
| gross_profit_factor | 0.9776 |
| gross_win_rate | 0.4990 |
| sharpe_ratio | -3.0265 |
| sortino_ratio | -0.9803 |
| max_drawdown | 0.6828 |
| cagr | -0.3610 |
| net_avg_win | 48.5738 |
| net_avg_loss | -74.9677 |
| avg_hold_time_bars | 6.3412 |
| exposure | 0.1461 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
