# EMA Hourly Continuation — DOGS/USDT P21_26

**Symbol:** DOGS/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1059 |
| net_profit_factor | 0.2004 |
| net_win_rate | 0.3437 |
| gross_profit_factor | 0.4911 |
| gross_win_rate | 0.3777 |
| sharpe_ratio | -14.9970 |
| sortino_ratio | -7.6280 |
| max_drawdown | 0.9999 |
| cagr | -0.9833 |
| net_avg_win | 6.8828 |
| net_avg_loss | -17.9911 |
| avg_hold_time_bars | 1.6771 |
| exposure | 0.0942 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
