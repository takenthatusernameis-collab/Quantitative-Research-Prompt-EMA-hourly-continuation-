# EMA Hourly Continuation — CARV/USDT P89_100

**Symbol:** CARV/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.2279 |
| net_win_rate | 0.3765 |
| gross_profit_factor | 0.7067 |
| gross_win_rate | 0.4388 |
| sharpe_ratio | -8.6100 |
| sortino_ratio | -2.8383 |
| max_drawdown | 0.9455 |
| cagr | -0.7592 |
| net_avg_win | 17.7521 |
| net_avg_loss | -47.0391 |
| avg_hold_time_bars | 2.7026 |
| exposure | 0.0634 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
