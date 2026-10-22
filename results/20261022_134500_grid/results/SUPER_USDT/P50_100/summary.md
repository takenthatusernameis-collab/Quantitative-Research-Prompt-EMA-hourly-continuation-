# EMA Hourly Continuation — SUPER/USDT P50_100

**Symbol:** SUPER/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 586 |
| net_profit_factor | 0.6220 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9651 |
| gross_win_rate | 0.5068 |
| sharpe_ratio | -3.2103 |
| sortino_ratio | -1.1078 |
| max_drawdown | 0.7449 |
| cagr | -0.4032 |
| net_avg_win | 40.8018 |
| net_avg_loss | -65.5949 |
| avg_hold_time_bars | 6.9795 |
| exposure | 0.1859 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
