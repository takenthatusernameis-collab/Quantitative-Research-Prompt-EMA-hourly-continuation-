# EMA Hourly Continuation — UQC/USDT P26_100

**Symbol:** UQC/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 312 |
| net_profit_factor | 0.2275 |
| net_win_rate | 0.2821 |
| gross_profit_factor | 0.4176 |
| gross_win_rate | 0.3013 |
| sharpe_ratio | -7.4233 |
| sortino_ratio | -1.8431 |
| max_drawdown | 0.9234 |
| cagr | -0.6389 |
| net_avg_win | 30.9069 |
| net_avg_loss | -53.3650 |
| avg_hold_time_bars | 38.4295 |
| exposure | 0.5427 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
