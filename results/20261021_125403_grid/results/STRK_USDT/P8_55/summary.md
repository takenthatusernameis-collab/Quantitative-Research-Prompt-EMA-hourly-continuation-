# EMA Hourly Continuation — STRK/USDT P8_55

**Symbol:** STRK/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.7914 |
| net_win_rate | 0.4878 |
| gross_profit_factor | 0.9616 |
| gross_win_rate | 0.4878 |
| sharpe_ratio | -2.0014 |
| sortino_ratio | -0.7317 |
| max_drawdown | 0.5953 |
| cagr | -0.2869 |
| net_avg_win | 67.8422 |
| net_avg_loss | -81.6441 |
| avg_hold_time_bars | 15.1280 |
| exposure | 0.4511 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
