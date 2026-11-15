# EMA Hourly Continuation — CERE/USDT P8_200

**Symbol:** CERE/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.5071 |
| net_win_rate | 0.3913 |
| gross_profit_factor | 0.7713 |
| gross_win_rate | 0.4071 |
| sharpe_ratio | -6.1455 |
| sortino_ratio | -1.9424 |
| max_drawdown | 0.9168 |
| cagr | -0.6198 |
| net_avg_win | 47.3722 |
| net_avg_loss | -60.0583 |
| avg_hold_time_bars | 32.4348 |
| exposure | 0.7460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
