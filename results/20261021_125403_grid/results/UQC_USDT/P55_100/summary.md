# EMA Hourly Continuation — UQC/USDT P55_100

**Symbol:** UQC/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 218 |
| net_profit_factor | 0.2902 |
| net_win_rate | 0.2706 |
| gross_profit_factor | 0.4478 |
| gross_win_rate | 0.2936 |
| sharpe_ratio | -5.9124 |
| sortino_ratio | -1.2251 |
| max_drawdown | 0.7968 |
| cagr | -0.4632 |
| net_avg_win | 54.8540 |
| net_avg_loss | -70.1518 |
| avg_hold_time_bars | 36.9954 |
| exposure | 0.3650 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
