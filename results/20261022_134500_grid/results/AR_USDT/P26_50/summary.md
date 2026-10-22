# EMA Hourly Continuation — AR/USDT P26_50

**Symbol:** AR/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 965 |
| net_profit_factor | 0.3837 |
| net_win_rate | 0.4394 |
| gross_profit_factor | 0.6660 |
| gross_win_rate | 0.4549 |
| sharpe_ratio | -7.4177 |
| sortino_ratio | -3.2500 |
| max_drawdown | 0.9817 |
| cagr | -0.7966 |
| net_avg_win | 14.4120 |
| net_avg_loss | -29.4409 |
| avg_hold_time_bars | 3.7689 |
| exposure | 0.1653 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
