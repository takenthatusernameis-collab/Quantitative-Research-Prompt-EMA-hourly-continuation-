# EMA Hourly Continuation — CSPR/USDT P20_100

**Symbol:** CSPR/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 951 |
| net_profit_factor | 0.4784 |
| net_win_rate | 0.4143 |
| gross_profit_factor | 0.8036 |
| gross_win_rate | 0.4248 |
| sharpe_ratio | -7.2517 |
| sortino_ratio | -3.1485 |
| max_drawdown | 0.9790 |
| cagr | -0.7806 |
| net_avg_win | 22.7654 |
| net_avg_loss | -33.6588 |
| avg_hold_time_bars | 9.1441 |
| exposure | 0.3953 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
