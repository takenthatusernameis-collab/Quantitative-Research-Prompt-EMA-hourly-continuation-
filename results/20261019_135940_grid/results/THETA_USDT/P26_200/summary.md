# EMA Hourly Continuation — THETA/USDT P26_200

**Symbol:** THETA/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.7011 |
| net_win_rate | 0.4897 |
| gross_profit_factor | 0.9763 |
| gross_win_rate | 0.4974 |
| sharpe_ratio | -2.0639 |
| sortino_ratio | -0.5764 |
| max_drawdown | 0.5148 |
| cagr | -0.2360 |
| net_avg_win | 60.6454 |
| net_avg_loss | -83.0105 |
| avg_hold_time_bars | 31.5644 |
| exposure | 0.5567 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
