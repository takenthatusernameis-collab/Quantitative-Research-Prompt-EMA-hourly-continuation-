# EMA Hourly Continuation — PIXEL/USDT P12_26

**Symbol:** PIXEL/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1388 |
| net_profit_factor | 0.5083 |
| net_win_rate | 0.4481 |
| gross_profit_factor | 0.9585 |
| gross_win_rate | 0.4604 |
| sharpe_ratio | -9.0387 |
| sortino_ratio | -4.7310 |
| max_drawdown | 0.9972 |
| cagr | -0.9025 |
| net_avg_win | 16.5734 |
| net_avg_loss | -26.4758 |
| avg_hold_time_bars | 3.5166 |
| exposure | 0.2209 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
