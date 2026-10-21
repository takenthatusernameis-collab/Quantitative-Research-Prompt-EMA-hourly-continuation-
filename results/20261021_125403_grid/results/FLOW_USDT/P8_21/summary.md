# EMA Hourly Continuation — FLOW/USDT P8_21

**Symbol:** FLOW/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 635 |
| net_profit_factor | 0.5628 |
| net_win_rate | 0.4614 |
| gross_profit_factor | 0.8183 |
| gross_win_rate | 0.4614 |
| sharpe_ratio | -4.0977 |
| sortino_ratio | -1.4770 |
| max_drawdown | 0.8185 |
| cagr | -0.4912 |
| net_avg_win | 35.8781 |
| net_avg_loss | -54.6202 |
| avg_hold_time_bars | 5.2504 |
| exposure | 0.1515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
