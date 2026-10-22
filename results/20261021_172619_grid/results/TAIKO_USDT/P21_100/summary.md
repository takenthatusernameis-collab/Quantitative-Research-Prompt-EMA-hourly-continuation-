# EMA Hourly Continuation — TAIKO/USDT P21_100

**Symbol:** TAIKO/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.8320 |
| net_win_rate | 0.5195 |
| gross_profit_factor | 1.0665 |
| gross_win_rate | 0.5195 |
| sharpe_ratio | -1.2013 |
| sortino_ratio | -0.3713 |
| max_drawdown | 0.4160 |
| cagr | -0.1586 |
| net_avg_win | 73.4280 |
| net_avg_loss | -95.3990 |
| avg_hold_time_bars | 19.3112 |
| exposure | 0.4054 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
