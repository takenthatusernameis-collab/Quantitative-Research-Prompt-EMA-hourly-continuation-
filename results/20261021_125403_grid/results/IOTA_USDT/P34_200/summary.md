# EMA Hourly Continuation — IOTA/USDT P34_200

**Symbol:** IOTA/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.9273 |
| net_win_rate | 0.5296 |
| gross_profit_factor | 1.1227 |
| gross_win_rate | 0.5296 |
| sharpe_ratio | -0.3538 |
| sortino_ratio | -0.0864 |
| max_drawdown | 0.2124 |
| cagr | -0.0427 |
| net_avg_win | 87.1078 |
| net_avg_loss | -105.7619 |
| avg_hold_time_bars | 37.9652 |
| exposure | 0.4953 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
