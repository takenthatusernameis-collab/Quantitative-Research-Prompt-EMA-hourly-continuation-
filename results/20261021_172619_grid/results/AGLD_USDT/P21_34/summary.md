# EMA Hourly Continuation — AGLD/USDT P21_34

**Symbol:** AGLD/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 534 |
| net_profit_factor | 0.6946 |
| net_win_rate | 0.4925 |
| gross_profit_factor | 0.9895 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -2.8086 |
| sortino_ratio | -0.9298 |
| max_drawdown | 0.6857 |
| cagr | -0.3453 |
| net_avg_win | 56.7600 |
| net_avg_loss | -79.3053 |
| avg_hold_time_bars | 5.3427 |
| exposure | 0.1291 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
