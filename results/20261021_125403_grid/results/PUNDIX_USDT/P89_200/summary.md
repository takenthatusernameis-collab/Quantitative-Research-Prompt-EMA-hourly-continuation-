# EMA Hourly Continuation — PUNDIX/USDT P89_200

**Symbol:** PUNDIX/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.7472 |
| net_win_rate | 0.5084 |
| gross_profit_factor | 1.0510 |
| gross_win_rate | 0.5084 |
| sharpe_ratio | -1.6341 |
| sortino_ratio | -0.4045 |
| max_drawdown | 0.3855 |
| cagr | -0.1701 |
| net_avg_win | 72.7157 |
| net_avg_loss | -100.6225 |
| avg_hold_time_bars | 17.4883 |
| exposure | 0.2377 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
