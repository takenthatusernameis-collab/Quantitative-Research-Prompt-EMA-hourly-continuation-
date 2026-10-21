# EMA Hourly Continuation — IOTX/USDT P21_200

**Symbol:** IOTX/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.8097 |
| net_win_rate | 0.5013 |
| gross_profit_factor | 0.9856 |
| gross_win_rate | 0.5039 |
| sharpe_ratio | -1.1711 |
| sortino_ratio | -0.3271 |
| max_drawdown | 0.3971 |
| cagr | -0.1411 |
| net_avg_win | 70.7106 |
| net_avg_loss | -87.7940 |
| avg_hold_time_bars | 32.7087 |
| exposure | 0.5665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
