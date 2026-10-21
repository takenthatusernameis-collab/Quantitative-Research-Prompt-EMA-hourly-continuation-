# EMA Hourly Continuation — G/USDT P26_50

**Symbol:** G/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.5989 |
| net_win_rate | 0.4683 |
| gross_profit_factor | 0.9017 |
| gross_win_rate | 0.4683 |
| sharpe_ratio | -3.9701 |
| sortino_ratio | -1.3537 |
| max_drawdown | 0.7485 |
| cagr | -0.4614 |
| net_avg_win | 48.1957 |
| net_avg_loss | -70.8741 |
| avg_hold_time_bars | 6.8262 |
| exposure | 0.1755 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
