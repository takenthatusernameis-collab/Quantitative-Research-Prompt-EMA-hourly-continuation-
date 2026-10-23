# EMA Hourly Continuation — TNSR/USDT P26_200

**Symbol:** TNSR/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.6492 |
| net_win_rate | 0.4606 |
| gross_profit_factor | 0.8685 |
| gross_win_rate | 0.4630 |
| sharpe_ratio | -2.9424 |
| sortino_ratio | -0.8538 |
| max_drawdown | 0.6586 |
| cagr | -0.3364 |
| net_avg_win | 59.9446 |
| net_avg_loss | -78.8601 |
| avg_hold_time_bars | 28.9329 |
| exposure | 0.5656 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
