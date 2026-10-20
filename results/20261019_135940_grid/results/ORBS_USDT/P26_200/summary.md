# EMA Hourly Continuation — ORBS/USDT P26_200

**Symbol:** ORBS/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.6058 |
| net_win_rate | 0.4444 |
| gross_profit_factor | 0.9178 |
| gross_win_rate | 0.4583 |
| sharpe_ratio | -3.8088 |
| sortino_ratio | -1.1042 |
| max_drawdown | 0.7473 |
| cagr | -0.4146 |
| net_avg_win | 59.1776 |
| net_avg_loss | -78.1506 |
| avg_hold_time_bars | 30.1644 |
| exposure | 0.5923 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
