# EMA Hourly Continuation — BLUR/USDT P8_50

**Symbol:** BLUR/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1017 |
| net_profit_factor | 0.6549 |
| net_win_rate | 0.4907 |
| gross_profit_factor | 1.0080 |
| gross_win_rate | 0.4995 |
| sharpe_ratio | -4.5935 |
| sortino_ratio | -2.0632 |
| max_drawdown | 0.9189 |
| cagr | -0.6258 |
| net_avg_win | 34.8422 |
| net_avg_loss | -51.2516 |
| avg_hold_time_bars | 10.6568 |
| exposure | 0.4904 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
