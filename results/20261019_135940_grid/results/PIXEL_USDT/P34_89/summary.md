# EMA Hourly Continuation — PIXEL/USDT P34_89

**Symbol:** PIXEL/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 685 |
| net_profit_factor | 0.6418 |
| net_win_rate | 0.4701 |
| gross_profit_factor | 0.9506 |
| gross_win_rate | 0.4788 |
| sharpe_ratio | -3.9359 |
| sortino_ratio | -1.4499 |
| max_drawdown | 0.8363 |
| cagr | -0.4981 |
| net_avg_win | 45.8702 |
| net_avg_loss | -63.3972 |
| avg_hold_time_bars | 7.9474 |
| exposure | 0.2463 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
