# EMA Hourly Continuation — ROSE/USDT P50_55

**Symbol:** ROSE/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 858 |
| net_profit_factor | 0.2721 |
| net_win_rate | 0.3671 |
| gross_profit_factor | 0.7914 |
| gross_win_rate | 0.4126 |
| sharpe_ratio | -11.9207 |
| sortino_ratio | -5.0743 |
| max_drawdown | 0.9989 |
| cagr | -0.9341 |
| net_avg_win | 11.8530 |
| net_avg_loss | -25.2723 |
| avg_hold_time_bars | 1.9918 |
| exposure | 0.0777 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
