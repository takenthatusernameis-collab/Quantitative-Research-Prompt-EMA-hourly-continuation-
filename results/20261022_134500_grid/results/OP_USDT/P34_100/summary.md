# EMA Hourly Continuation — OP/USDT P34_100

**Symbol:** OP/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 629 |
| net_profit_factor | 0.5958 |
| net_win_rate | 0.4722 |
| gross_profit_factor | 0.9002 |
| gross_win_rate | 0.4801 |
| sharpe_ratio | -3.8384 |
| sortino_ratio | -1.3622 |
| max_drawdown | 0.8082 |
| cagr | -0.4727 |
| net_avg_win | 39.6798 |
| net_avg_loss | -59.5809 |
| avg_hold_time_bars | 10.0461 |
| exposure | 0.2872 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
