# EMA Hourly Continuation — IOTX/USDT P55_200

**Symbol:** IOTX/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.7919 |
| net_win_rate | 0.5016 |
| gross_profit_factor | 0.9833 |
| gross_win_rate | 0.5047 |
| sharpe_ratio | -1.1550 |
| sortino_ratio | -0.2944 |
| max_drawdown | 0.3411 |
| cagr | -0.1275 |
| net_avg_win | 69.4335 |
| net_avg_loss | -88.2325 |
| avg_hold_time_bars | 25.3628 |
| exposure | 0.3655 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
