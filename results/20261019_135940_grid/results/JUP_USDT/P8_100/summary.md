# EMA Hourly Continuation — JUP/USDT P8_100

**Symbol:** JUP/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 645 |
| net_profit_factor | 0.6266 |
| net_win_rate | 0.4620 |
| gross_profit_factor | 0.8956 |
| gross_win_rate | 0.4682 |
| sharpe_ratio | -3.7561 |
| sortino_ratio | -1.3397 |
| max_drawdown | 0.8082 |
| cagr | -0.4714 |
| net_avg_win | 44.9480 |
| net_avg_loss | -61.6057 |
| avg_hold_time_bars | 22.4434 |
| exposure | 0.6580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
