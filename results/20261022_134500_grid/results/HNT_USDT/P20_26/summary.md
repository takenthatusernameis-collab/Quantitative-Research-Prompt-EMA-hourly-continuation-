# EMA Hourly Continuation — HNT/USDT P20_26

**Symbol:** HNT/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1237 |
| net_profit_factor | 0.2311 |
| net_win_rate | 0.3460 |
| gross_profit_factor | 0.6213 |
| gross_win_rate | 0.3791 |
| sharpe_ratio | -14.3512 |
| sortino_ratio | -7.2623 |
| max_drawdown | 0.9999 |
| cagr | -0.9776 |
| net_avg_win | 7.0207 |
| net_avg_loss | -16.0744 |
| avg_hold_time_bars | 2.0485 |
| exposure | 0.1152 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
