# EMA Hourly Continuation — CETUS/USDT P26_100

**Symbol:** CETUS/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.7972 |
| net_win_rate | 0.4887 |
| gross_profit_factor | 0.9747 |
| gross_win_rate | 0.4887 |
| sharpe_ratio | -1.7618 |
| sortino_ratio | -0.5536 |
| max_drawdown | 0.5041 |
| cagr | -0.2270 |
| net_avg_win | 78.9205 |
| net_avg_loss | -94.6198 |
| avg_hold_time_bars | 15.6632 |
| exposure | 0.3452 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
