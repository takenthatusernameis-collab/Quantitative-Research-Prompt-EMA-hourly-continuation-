# EMA Hourly Continuation — SAND/USDT P8_100

**Symbol:** SAND/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.5411 |
| net_win_rate | 0.4389 |
| gross_profit_factor | 0.8318 |
| gross_win_rate | 0.4489 |
| sharpe_ratio | -4.4578 |
| sortino_ratio | -1.3931 |
| max_drawdown | 0.8221 |
| cagr | -0.4935 |
| net_avg_win | 44.0798 |
| net_avg_loss | -63.7201 |
| avg_hold_time_bars | 32.8116 |
| exposure | 0.7442 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
