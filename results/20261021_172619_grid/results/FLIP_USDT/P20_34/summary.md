# EMA Hourly Continuation — FLIP/USDT P20_34

**Symbol:** FLIP/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.5183 |
| net_win_rate | 0.4510 |
| gross_profit_factor | 0.9193 |
| gross_win_rate | 0.4715 |
| sharpe_ratio | -4.7531 |
| sortino_ratio | -1.4128 |
| max_drawdown | 0.8210 |
| cagr | -0.4923 |
| net_avg_win | 44.4334 |
| net_avg_loss | -70.4364 |
| avg_hold_time_bars | 8.1754 |
| exposure | 0.1631 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
