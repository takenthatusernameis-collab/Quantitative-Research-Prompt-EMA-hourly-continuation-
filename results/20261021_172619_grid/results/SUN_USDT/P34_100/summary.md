# EMA Hourly Continuation — SUN/USDT P34_100

**Symbol:** SUN/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.4877 |
| net_win_rate | 0.4243 |
| gross_profit_factor | 0.8316 |
| gross_win_rate | 0.4404 |
| sharpe_ratio | -5.3806 |
| sortino_ratio | -1.5961 |
| max_drawdown | 0.8586 |
| cagr | -0.5347 |
| net_avg_win | 43.9815 |
| net_avg_loss | -66.4729 |
| avg_hold_time_bars | 13.7225 |
| exposure | 0.2707 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
