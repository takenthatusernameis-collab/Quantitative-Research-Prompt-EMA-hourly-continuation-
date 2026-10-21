# EMA Hourly Continuation — DOGE/USDT P26_100

**Symbol:** DOGE/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.6956 |
| net_win_rate | 0.4812 |
| gross_profit_factor | 0.9198 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -2.2505 |
| sortino_ratio | -0.6418 |
| max_drawdown | 0.5565 |
| cagr | -0.2552 |
| net_avg_win | 62.2396 |
| net_avg_loss | -82.9870 |
| avg_hold_time_bars | 18.7995 |
| exposure | 0.3410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
