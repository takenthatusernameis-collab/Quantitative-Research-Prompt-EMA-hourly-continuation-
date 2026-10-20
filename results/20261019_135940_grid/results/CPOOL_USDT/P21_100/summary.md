# EMA Hourly Continuation — CPOOL/USDT P21_100

**Symbol:** CPOOL/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 732 |
| net_profit_factor | 0.6548 |
| net_win_rate | 0.4645 |
| gross_profit_factor | 0.8951 |
| gross_win_rate | 0.4713 |
| sharpe_ratio | -4.0321 |
| sortino_ratio | -1.5287 |
| max_drawdown | 0.8538 |
| cagr | -0.5209 |
| net_avg_win | 46.9986 |
| net_avg_loss | -62.2549 |
| avg_hold_time_bars | 11.0137 |
| exposure | 0.3665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
