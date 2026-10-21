# EMA Hourly Continuation — BNB/USDT P26_50

**Symbol:** BNB/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.5550 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9988 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -3.4006 |
| sortino_ratio | -0.9311 |
| max_drawdown | 0.6673 |
| cagr | -0.3465 |
| net_avg_win | 45.7279 |
| net_avg_loss | -82.3979 |
| avg_hold_time_bars | 6.6425 |
| exposure | 0.1081 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
