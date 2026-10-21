# EMA Hourly Continuation — IOTX/USDT P21_26

**Symbol:** IOTX/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 196 |
| net_profit_factor | 0.6002 |
| net_win_rate | 0.4745 |
| gross_profit_factor | 0.8844 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -2.1406 |
| sortino_ratio | -0.4299 |
| max_drawdown | 0.4025 |
| cagr | -0.1786 |
| net_avg_win | 62.9408 |
| net_avg_loss | -94.6904 |
| avg_hold_time_bars | 5.0204 |
| exposure | 0.0447 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
