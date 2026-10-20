# EMA Hourly Continuation — SUSHI/USDT P26_200

**Symbol:** SUSHI/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.6375 |
| net_win_rate | 0.4701 |
| gross_profit_factor | 0.9007 |
| gross_win_rate | 0.4779 |
| sharpe_ratio | -2.6838 |
| sortino_ratio | -0.7427 |
| max_drawdown | 0.5994 |
| cagr | -0.2944 |
| net_avg_win | 56.8418 |
| net_avg_loss | -79.1160 |
| avg_hold_time_bars | 34.1091 |
| exposure | 0.5942 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
