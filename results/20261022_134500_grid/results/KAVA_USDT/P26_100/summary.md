# EMA Hourly Continuation — KAVA/USDT P26_100

**Symbol:** KAVA/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.5430 |
| net_win_rate | 0.4438 |
| gross_profit_factor | 0.9264 |
| gross_win_rate | 0.4660 |
| sharpe_ratio | -6.0494 |
| sortino_ratio | -2.2040 |
| max_drawdown | 0.9399 |
| cagr | -0.6648 |
| net_avg_win | 37.0551 |
| net_avg_loss | -54.4519 |
| avg_hold_time_bars | 12.3905 |
| exposure | 0.3807 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
