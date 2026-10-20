# EMA Hourly Continuation — CPOOL/USDT P34_100

**Symbol:** CPOOL/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 715 |
| net_profit_factor | 0.6159 |
| net_win_rate | 0.4587 |
| gross_profit_factor | 0.8506 |
| gross_win_rate | 0.4657 |
| sharpe_ratio | -4.3755 |
| sortino_ratio | -1.6471 |
| max_drawdown | 0.8702 |
| cagr | -0.5442 |
| net_avg_win | 42.0863 |
| net_avg_loss | -57.9178 |
| avg_hold_time_bars | 6.7063 |
| exposure | 0.2180 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
