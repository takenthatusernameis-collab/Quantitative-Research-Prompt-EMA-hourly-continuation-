# EMA Hourly Continuation — IOST/USDT P8_200

**Symbol:** IOST/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.7893 |
| net_win_rate | 0.5299 |
| gross_profit_factor | 1.1532 |
| gross_win_rate | 0.5380 |
| sharpe_ratio | -1.3145 |
| sortino_ratio | -0.3540 |
| max_drawdown | 0.3932 |
| cagr | -0.1585 |
| net_avg_win | 67.5392 |
| net_avg_loss | -96.4530 |
| avg_hold_time_bars | 48.1440 |
| exposure | 0.8053 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
