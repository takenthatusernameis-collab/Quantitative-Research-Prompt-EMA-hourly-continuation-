# EMA Hourly Continuation — MAGIC/USDT P12_34

**Symbol:** MAGIC/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 709 |
| net_profit_factor | 0.7195 |
| net_win_rate | 0.4824 |
| gross_profit_factor | 0.9737 |
| gross_win_rate | 0.4824 |
| sharpe_ratio | -3.2418 |
| sortino_ratio | -1.2337 |
| max_drawdown | 0.7776 |
| cagr | -0.4330 |
| net_avg_win | 56.9540 |
| net_avg_loss | -73.7687 |
| avg_hold_time_bars | 7.5021 |
| exposure | 0.2418 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
