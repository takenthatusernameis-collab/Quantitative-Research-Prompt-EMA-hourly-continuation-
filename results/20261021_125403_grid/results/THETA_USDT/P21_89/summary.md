# EMA Hourly Continuation — THETA/USDT P21_89

**Symbol:** THETA/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.7843 |
| net_win_rate | 0.4926 |
| gross_profit_factor | 0.9715 |
| gross_win_rate | 0.4926 |
| sharpe_ratio | -1.6924 |
| sortino_ratio | -0.5276 |
| max_drawdown | 0.5008 |
| cagr | -0.2160 |
| net_avg_win | 71.0401 |
| net_avg_loss | -87.9497 |
| avg_hold_time_bars | 15.2863 |
| exposure | 0.3300 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
