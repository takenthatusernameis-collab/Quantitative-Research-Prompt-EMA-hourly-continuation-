# EMA Hourly Continuation — TRX/USDT P8_200

**Symbol:** TRX/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.4709 |
| net_win_rate | 0.4469 |
| gross_profit_factor | 0.9925 |
| gross_win_rate | 0.4967 |
| sharpe_ratio | -5.5814 |
| sortino_ratio | -1.6613 |
| max_drawdown | 0.8928 |
| cagr | -0.5843 |
| net_avg_win | 38.4302 |
| net_avg_loss | -65.9340 |
| avg_hold_time_bars | 35.3341 |
| exposure | 0.7404 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
