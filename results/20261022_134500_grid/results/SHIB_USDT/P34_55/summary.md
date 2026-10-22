# EMA Hourly Continuation — SHIB/USDT P34_55

**Symbol:** SHIB/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 895 |
| net_profit_factor | 0.3754 |
| net_win_rate | 0.4156 |
| gross_profit_factor | 0.7960 |
| gross_win_rate | 0.4380 |
| sharpe_ratio | -9.7417 |
| sortino_ratio | -4.1760 |
| max_drawdown | 0.9952 |
| cagr | -0.8779 |
| net_avg_win | 16.0725 |
| net_avg_loss | -30.4552 |
| avg_hold_time_bars | 2.9989 |
| exposure | 0.1220 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
