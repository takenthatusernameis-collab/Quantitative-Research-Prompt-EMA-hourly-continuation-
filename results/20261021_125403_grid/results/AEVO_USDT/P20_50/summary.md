# EMA Hourly Continuation — AEVO/USDT P20_50

**Symbol:** AEVO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 588 |
| net_profit_factor | 0.6764 |
| net_win_rate | 0.4694 |
| gross_profit_factor | 0.8794 |
| gross_win_rate | 0.4694 |
| sharpe_ratio | -3.0763 |
| sortino_ratio | -1.0613 |
| max_drawdown | 0.7146 |
| cagr | -0.3851 |
| net_avg_win | 53.5314 |
| net_avg_loss | -70.0081 |
| avg_hold_time_bars | 7.5867 |
| exposure | 0.2019 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
