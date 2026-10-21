# EMA Hourly Continuation — DOGE/USDT P89_100

**Symbol:** DOGE/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 79 |
| net_profit_factor | 0.4839 |
| net_win_rate | 0.4304 |
| gross_profit_factor | 0.7248 |
| gross_win_rate | 0.4304 |
| sharpe_ratio | -1.8457 |
| sortino_ratio | -0.2347 |
| max_drawdown | 0.2489 |
| cagr | -0.1023 |
| net_avg_win | 65.4729 |
| net_avg_loss | -102.2281 |
| avg_hold_time_bars | 4.7089 |
| exposure | 0.0169 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
