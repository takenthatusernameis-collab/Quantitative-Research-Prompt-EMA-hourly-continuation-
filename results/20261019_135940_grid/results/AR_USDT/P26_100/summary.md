# EMA Hourly Continuation — AR/USDT P26_100

**Symbol:** AR/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 638 |
| net_profit_factor | 0.6112 |
| net_win_rate | 0.4702 |
| gross_profit_factor | 0.8914 |
| gross_win_rate | 0.4796 |
| sharpe_ratio | -3.6884 |
| sortino_ratio | -1.3131 |
| max_drawdown | 0.7978 |
| cagr | -0.4654 |
| net_avg_win | 41.5288 |
| net_avg_loss | -60.3061 |
| avg_hold_time_bars | 12.1003 |
| exposure | 0.3509 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
