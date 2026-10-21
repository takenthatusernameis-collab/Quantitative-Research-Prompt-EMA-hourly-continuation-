# EMA Hourly Continuation — FIDA/USDT P8_50

**Symbol:** FIDA/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 744 |
| net_profit_factor | 0.7551 |
| net_win_rate | 0.4933 |
| gross_profit_factor | 0.9667 |
| gross_win_rate | 0.4933 |
| sharpe_ratio | -2.3987 |
| sortino_ratio | -0.9332 |
| max_drawdown | 0.6663 |
| cagr | -0.3491 |
| net_avg_win | 55.5656 |
| net_avg_loss | -71.6386 |
| avg_hold_time_bars | 13.6169 |
| exposure | 0.4584 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
