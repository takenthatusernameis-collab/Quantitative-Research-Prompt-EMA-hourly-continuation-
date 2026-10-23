# EMA Hourly Continuation — ETN/USDT P21_26

**Symbol:** ETN/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1061 |
| net_profit_factor | 0.1590 |
| net_win_rate | 0.2526 |
| gross_profit_factor | 0.3293 |
| gross_win_rate | 0.2988 |
| sharpe_ratio | -18.2780 |
| sortino_ratio | -9.6123 |
| max_drawdown | 1.0000 |
| cagr | -0.9948 |
| net_avg_win | 7.0552 |
| net_avg_loss | -14.9945 |
| avg_hold_time_bars | 2.2630 |
| exposure | 0.1304 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
