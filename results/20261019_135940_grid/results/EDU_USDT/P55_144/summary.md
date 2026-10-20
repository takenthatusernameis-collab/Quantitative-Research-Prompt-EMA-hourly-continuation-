# EMA Hourly Continuation — EDU/USDT P55_144

**Symbol:** EDU/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 562 |
| net_profit_factor | 0.6092 |
| net_win_rate | 0.4662 |
| gross_profit_factor | 0.8729 |
| gross_win_rate | 0.4698 |
| sharpe_ratio | -3.7195 |
| sortino_ratio | -1.2396 |
| max_drawdown | 0.7817 |
| cagr | -0.4460 |
| net_avg_win | 46.0773 |
| net_avg_loss | -66.0606 |
| avg_hold_time_bars | 9.4698 |
| exposure | 0.2408 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
