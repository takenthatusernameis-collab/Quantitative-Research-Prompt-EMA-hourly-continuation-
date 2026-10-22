# EMA Hourly Continuation — TAIKO/USDT P89_100

**Symbol:** TAIKO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 91 |
| net_profit_factor | 0.6982 |
| net_win_rate | 0.5165 |
| gross_profit_factor | 1.0557 |
| gross_win_rate | 0.5165 |
| sharpe_ratio | -1.0588 |
| sortino_ratio | -0.1496 |
| max_drawdown | 0.1726 |
| cagr | -0.0662 |
| net_avg_win | 73.9792 |
| net_avg_loss | -113.1733 |
| avg_hold_time_bars | 5.1319 |
| exposure | 0.0224 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
