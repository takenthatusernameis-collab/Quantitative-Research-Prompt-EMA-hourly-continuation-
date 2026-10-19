# EMA Hourly Continuation — SHIB/USDT P12_26

**Symbol:** SHIB/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1395 |
| net_profit_factor | 0.2814 |
| net_win_rate | 0.4258 |
| gross_profit_factor | 0.7589 |
| gross_win_rate | 0.4616 |
| sharpe_ratio | -12.3408 |
| sortino_ratio | -6.5289 |
| max_drawdown | 0.9998 |
| cagr | -0.9671 |
| net_avg_win | 6.5927 |
| net_avg_loss | -17.3710 |
| avg_hold_time_bars | 2.7806 |
| exposure | 0.1763 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
