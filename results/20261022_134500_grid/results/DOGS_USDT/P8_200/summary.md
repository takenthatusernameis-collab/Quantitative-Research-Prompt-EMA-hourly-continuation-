# EMA Hourly Continuation — DOGS/USDT P8_200

**Symbol:** DOGS/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.6442 |
| net_win_rate | 0.4741 |
| gross_profit_factor | 0.9121 |
| gross_win_rate | 0.4741 |
| sharpe_ratio | -2.9881 |
| sortino_ratio | -0.8632 |
| max_drawdown | 0.6198 |
| cagr | -0.3421 |
| net_avg_win | 61.8006 |
| net_avg_loss | -86.4855 |
| avg_hold_time_bars | 40.3161 |
| exposure | 0.7849 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
