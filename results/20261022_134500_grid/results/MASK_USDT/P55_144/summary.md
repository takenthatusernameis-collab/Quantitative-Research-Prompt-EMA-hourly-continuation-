# EMA Hourly Continuation — MASK/USDT P55_144

**Symbol:** MASK/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 561 |
| net_profit_factor | 0.5073 |
| net_win_rate | 0.4706 |
| gross_profit_factor | 0.9204 |
| gross_win_rate | 0.4777 |
| sharpe_ratio | -4.7560 |
| sortino_ratio | -1.5751 |
| max_drawdown | 0.8609 |
| cagr | -0.5422 |
| net_avg_win | 33.5228 |
| net_avg_loss | -58.7343 |
| avg_hold_time_bars | 9.5169 |
| exposure | 0.2427 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
