# EMA Hourly Continuation — AVA/USDT P12_21

**Symbol:** AVA/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1377 |
| net_profit_factor | 0.2306 |
| net_win_rate | 0.3929 |
| gross_profit_factor | 0.6592 |
| gross_win_rate | 0.4248 |
| sharpe_ratio | -13.5433 |
| sortino_ratio | -7.2058 |
| max_drawdown | 0.9999 |
| cagr | -0.9763 |
| net_avg_win | 5.5409 |
| net_avg_loss | -15.5464 |
| avg_hold_time_bars | 2.4198 |
| exposure | 0.1515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
