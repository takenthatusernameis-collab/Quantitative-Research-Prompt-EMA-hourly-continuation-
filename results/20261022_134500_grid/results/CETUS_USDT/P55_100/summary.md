# EMA Hourly Continuation — CETUS/USDT P55_100

**Symbol:** CETUS/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 618 |
| net_profit_factor | 0.6180 |
| net_win_rate | 0.4709 |
| gross_profit_factor | 0.9582 |
| gross_win_rate | 0.4790 |
| sharpe_ratio | -4.2322 |
| sortino_ratio | -1.4857 |
| max_drawdown | 0.8334 |
| cagr | -0.5069 |
| net_avg_win | 46.2447 |
| net_avg_loss | -66.5951 |
| avg_hold_time_bars | 5.5421 |
| exposure | 0.1550 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
