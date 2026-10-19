# EMA Hourly Continuation — ATOM/USDT P8_100

**Symbol:** ATOM/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.6904 |
| net_win_rate | 0.5085 |
| gross_profit_factor | 1.0859 |
| gross_win_rate | 0.5191 |
| sharpe_ratio | -2.4493 |
| sortino_ratio | -0.7461 |
| max_drawdown | 0.6105 |
| cagr | -0.3021 |
| net_avg_win | 55.4925 |
| net_avg_loss | -83.1582 |
| avg_hold_time_bars | 34.5830 |
| exposure | 0.7388 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
