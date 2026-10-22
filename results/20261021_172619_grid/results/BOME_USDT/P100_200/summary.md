# EMA Hourly Continuation — BOME/USDT P100_200

**Symbol:** BOME/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 253 |
| net_profit_factor | 0.7319 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 0.8811 |
| gross_win_rate | 0.4783 |
| sharpe_ratio | -1.3695 |
| sortino_ratio | -0.3104 |
| max_drawdown | 0.3672 |
| cagr | -0.1330 |
| net_avg_win | 67.9424 |
| net_avg_loss | -85.0987 |
| avg_hold_time_bars | 14.2490 |
| exposure | 0.1639 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
