# EMA Hourly Continuation — FLOKI/USDT P26_200

**Symbol:** FLOKI/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 253 |
| net_profit_factor | 0.7684 |
| net_win_rate | 0.4704 |
| gross_profit_factor | 0.8937 |
| gross_win_rate | 0.4704 |
| sharpe_ratio | -1.3474 |
| sortino_ratio | -0.3046 |
| max_drawdown | 0.3192 |
| cagr | -0.1318 |
| net_avg_win | 83.3075 |
| net_avg_loss | -96.2804 |
| avg_hold_time_bars | 54.1937 |
| exposure | 0.6232 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
