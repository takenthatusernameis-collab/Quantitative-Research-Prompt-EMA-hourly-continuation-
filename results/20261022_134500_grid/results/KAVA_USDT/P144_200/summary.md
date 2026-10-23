# EMA Hourly Continuation — KAVA/USDT P144_200

**Symbol:** KAVA/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.3566 |
| net_win_rate | 0.3911 |
| gross_profit_factor | 0.7509 |
| gross_win_rate | 0.4311 |
| sharpe_ratio | -7.0431 |
| sortino_ratio | -2.1447 |
| max_drawdown | 0.9352 |
| cagr | -0.6616 |
| net_avg_win | 29.4203 |
| net_avg_loss | -52.9921 |
| avg_hold_time_bars | 4.7356 |
| exposure | 0.0969 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
