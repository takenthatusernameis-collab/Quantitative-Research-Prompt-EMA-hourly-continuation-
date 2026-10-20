# EMA Hourly Continuation — BAND/USDT P89_100

**Symbol:** BAND/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 546 |
| net_profit_factor | 0.2567 |
| net_win_rate | 0.3901 |
| gross_profit_factor | 0.8058 |
| gross_win_rate | 0.4597 |
| sharpe_ratio | -8.4562 |
| sortino_ratio | -2.8422 |
| max_drawdown | 0.9754 |
| cagr | -0.7685 |
| net_avg_win | 15.8109 |
| net_avg_loss | -39.3945 |
| avg_hold_time_bars | 2.4982 |
| exposure | 0.0617 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
