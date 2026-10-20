# EMA Hourly Continuation — ZETA/USDT P50_55

**Symbol:** ZETA/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 829 |
| net_profit_factor | 0.2809 |
| net_win_rate | 0.3546 |
| gross_profit_factor | 0.7774 |
| gross_win_rate | 0.4005 |
| sharpe_ratio | -12.1314 |
| sortino_ratio | -5.0847 |
| max_drawdown | 0.9990 |
| cagr | -0.9347 |
| net_avg_win | 13.2731 |
| net_avg_loss | -25.9664 |
| avg_hold_time_bars | 2.1592 |
| exposure | 0.0810 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
