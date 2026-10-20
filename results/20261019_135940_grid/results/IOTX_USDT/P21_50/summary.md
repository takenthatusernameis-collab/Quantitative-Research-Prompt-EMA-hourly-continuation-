# EMA Hourly Continuation — IOTX/USDT P21_50

**Symbol:** IOTX/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1001 |
| net_profit_factor | 0.5327 |
| net_win_rate | 0.4565 |
| gross_profit_factor | 0.9725 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -7.3971 |
| sortino_ratio | -3.3042 |
| max_drawdown | 0.9837 |
| cagr | -0.8026 |
| net_avg_win | 24.5167 |
| net_avg_loss | -38.6658 |
| avg_hold_time_bars | 4.2647 |
| exposure | 0.1940 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
