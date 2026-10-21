# EMA Hourly Continuation — ONDO/USDT P20_34

**Symbol:** ONDO/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 0.7988 |
| net_win_rate | 0.5150 |
| gross_profit_factor | 1.0640 |
| gross_win_rate | 0.5150 |
| sharpe_ratio | -1.1618 |
| sortino_ratio | -0.2729 |
| max_drawdown | 0.3220 |
| cagr | -0.1180 |
| net_avg_win | 78.4056 |
| net_avg_loss | -104.2357 |
| avg_hold_time_bars | 5.7368 |
| exposure | 0.0694 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
