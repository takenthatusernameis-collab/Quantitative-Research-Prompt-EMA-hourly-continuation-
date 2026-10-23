# EMA Hourly Continuation — PEOPLE/USDT P8_55

**Symbol:** PEOPLE/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 914 |
| net_profit_factor | 0.6016 |
| net_win_rate | 0.4551 |
| gross_profit_factor | 0.8558 |
| gross_win_rate | 0.4628 |
| sharpe_ratio | -5.1039 |
| sortino_ratio | -2.1656 |
| max_drawdown | 0.9246 |
| cagr | -0.6412 |
| net_avg_win | 33.5624 |
| net_avg_loss | -46.6033 |
| avg_hold_time_bars | 12.6794 |
| exposure | 0.5244 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
