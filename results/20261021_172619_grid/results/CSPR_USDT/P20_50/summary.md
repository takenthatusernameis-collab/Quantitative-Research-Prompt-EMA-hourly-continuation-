# EMA Hourly Continuation — CSPR/USDT P20_50

**Symbol:** CSPR/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.6631 |
| net_win_rate | 0.4571 |
| gross_profit_factor | 0.8605 |
| gross_win_rate | 0.4571 |
| sharpe_ratio | -2.9116 |
| sortino_ratio | -0.8943 |
| max_drawdown | 0.6431 |
| cagr | -0.3365 |
| net_avg_win | 59.4143 |
| net_avg_loss | -75.4383 |
| avg_hold_time_bars | 7.0451 |
| exposure | 0.1492 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
