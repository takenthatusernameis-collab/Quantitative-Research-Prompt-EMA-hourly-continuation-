# EMA Hourly Continuation — ATOM/USDT P8_21

**Symbol:** ATOM/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.6928 |
| net_win_rate | 0.4913 |
| gross_profit_factor | 1.0071 |
| gross_win_rate | 0.4913 |
| sharpe_ratio | -2.9072 |
| sortino_ratio | -0.9518 |
| max_drawdown | 0.6661 |
| cagr | -0.3516 |
| net_avg_win | 58.6490 |
| net_avg_loss | -81.7684 |
| avg_hold_time_bars | 5.4855 |
| exposure | 0.1294 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
