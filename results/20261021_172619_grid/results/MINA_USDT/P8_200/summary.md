# EMA Hourly Continuation — MINA/USDT P8_200

**Symbol:** MINA/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.9385 |
| net_win_rate | 0.5276 |
| gross_profit_factor | 1.0996 |
| gross_win_rate | 0.5276 |
| sharpe_ratio | -0.2819 |
| sortino_ratio | -0.0691 |
| max_drawdown | 0.2936 |
| cagr | -0.0354 |
| net_avg_win | 86.3705 |
| net_avg_loss | -102.7799 |
| avg_hold_time_bars | 61.0241 |
| exposure | 0.8044 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
