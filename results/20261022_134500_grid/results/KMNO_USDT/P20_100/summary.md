# EMA Hourly Continuation — KMNO/USDT P20_100

**Symbol:** KMNO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 547 |
| net_profit_factor | 0.6510 |
| net_win_rate | 0.4662 |
| gross_profit_factor | 0.9230 |
| gross_win_rate | 0.4717 |
| sharpe_ratio | -3.6109 |
| sortino_ratio | -1.1948 |
| max_drawdown | 0.7613 |
| cagr | -0.4365 |
| net_avg_win | 55.4396 |
| net_avg_loss | -74.3673 |
| avg_hold_time_bars | 16.6929 |
| exposure | 0.4216 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
