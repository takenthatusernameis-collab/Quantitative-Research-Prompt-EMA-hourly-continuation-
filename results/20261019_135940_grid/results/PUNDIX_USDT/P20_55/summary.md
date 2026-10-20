# EMA Hourly Continuation — PUNDIX/USDT P20_55

**Symbol:** PUNDIX/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 962 |
| net_profit_factor | 0.4935 |
| net_win_rate | 0.4491 |
| gross_profit_factor | 0.8977 |
| gross_win_rate | 0.4636 |
| sharpe_ratio | -7.4388 |
| sortino_ratio | -3.2471 |
| max_drawdown | 0.9827 |
| cagr | -0.7990 |
| net_avg_win | 22.1525 |
| net_avg_loss | -36.5886 |
| avg_hold_time_bars | 6.3306 |
| exposure | 0.2768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
