# EMA Hourly Continuation — MASK/USDT P50_89

**Symbol:** MASK/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 401 |
| net_profit_factor | 0.5562 |
| net_win_rate | 0.4638 |
| gross_profit_factor | 0.8518 |
| gross_win_rate | 0.4713 |
| sharpe_ratio | -3.3901 |
| sortino_ratio | -0.9710 |
| max_drawdown | 0.6818 |
| cagr | -0.3596 |
| net_avg_win | 45.3845 |
| net_avg_loss | -70.5891 |
| avg_hold_time_bars | 7.1746 |
| exposure | 0.1308 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
