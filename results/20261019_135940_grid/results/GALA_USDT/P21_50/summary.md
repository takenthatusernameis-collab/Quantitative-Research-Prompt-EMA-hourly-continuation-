# EMA Hourly Continuation — GALA/USDT P21_50

**Symbol:** GALA/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1043 |
| net_profit_factor | 0.4622 |
| net_win_rate | 0.4286 |
| gross_profit_factor | 0.8048 |
| gross_win_rate | 0.4382 |
| sharpe_ratio | -7.9932 |
| sortino_ratio | -3.6638 |
| max_drawdown | 0.9889 |
| cagr | -0.8278 |
| net_avg_win | 18.9963 |
| net_avg_loss | -30.8235 |
| avg_hold_time_bars | 4.1390 |
| exposure | 0.1962 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
