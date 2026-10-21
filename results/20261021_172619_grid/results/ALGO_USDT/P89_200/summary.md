# EMA Hourly Continuation — ALGO/USDT P89_200

**Symbol:** ALGO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 250 |
| net_profit_factor | 0.6892 |
| net_win_rate | 0.4600 |
| gross_profit_factor | 0.8691 |
| gross_win_rate | 0.4600 |
| sharpe_ratio | -1.9563 |
| sortino_ratio | -0.4399 |
| max_drawdown | 0.4222 |
| cagr | -0.1832 |
| net_avg_win | 76.8155 |
| net_avg_loss | -94.9468 |
| avg_hold_time_bars | 14.7160 |
| exposure | 0.1672 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
