# EMA Hourly Continuation — ARPA/USDT P8_50

**Symbol:** ARPA/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1173 |
| net_profit_factor | 0.5542 |
| net_win_rate | 0.4331 |
| gross_profit_factor | 0.8964 |
| gross_win_rate | 0.4484 |
| sharpe_ratio | -7.9802 |
| sortino_ratio | -3.8364 |
| max_drawdown | 0.9913 |
| cagr | -0.8446 |
| net_avg_win | 24.2477 |
| net_avg_loss | -33.4234 |
| avg_hold_time_bars | 8.5592 |
| exposure | 0.4543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
