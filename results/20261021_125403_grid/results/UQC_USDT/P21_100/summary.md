# EMA Hourly Continuation — UQC/USDT P21_100

**Symbol:** UQC/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 244 |
| net_profit_factor | 0.3517 |
| net_win_rate | 0.3033 |
| gross_profit_factor | 0.5197 |
| gross_win_rate | 0.3279 |
| sharpe_ratio | -5.6527 |
| sortino_ratio | -1.2229 |
| max_drawdown | 0.8016 |
| cagr | -0.4734 |
| net_avg_win | 58.7654 |
| net_avg_loss | -72.7337 |
| avg_hold_time_bars | 53.0123 |
| exposure | 0.5854 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
