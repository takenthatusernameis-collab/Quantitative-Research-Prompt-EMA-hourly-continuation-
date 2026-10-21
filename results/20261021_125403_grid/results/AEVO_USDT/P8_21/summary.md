# EMA Hourly Continuation — AEVO/USDT P8_21

**Symbol:** AEVO/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 723 |
| net_profit_factor | 0.7538 |
| net_win_rate | 0.5035 |
| gross_profit_factor | 1.0094 |
| gross_win_rate | 0.5035 |
| sharpe_ratio | -2.5050 |
| sortino_ratio | -0.9649 |
| max_drawdown | 0.6947 |
| cagr | -0.3573 |
| net_avg_win | 56.5508 |
| net_avg_loss | -76.0623 |
| avg_hold_time_bars | 5.6999 |
| exposure | 0.1865 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
