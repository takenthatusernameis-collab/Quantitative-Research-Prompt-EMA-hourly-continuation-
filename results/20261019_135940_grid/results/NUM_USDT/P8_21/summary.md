# EMA Hourly Continuation — NUM/USDT P8_21

**Symbol:** NUM/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1489 |
| net_profit_factor | 0.3381 |
| net_win_rate | 0.3311 |
| gross_profit_factor | 0.7624 |
| gross_win_rate | 0.3559 |
| sharpe_ratio | -15.2240 |
| sortino_ratio | -8.3902 |
| max_drawdown | 1.0000 |
| cagr | -0.9859 |
| net_avg_win | 10.3630 |
| net_avg_loss | -15.1694 |
| avg_hold_time_bars | 3.7381 |
| exposure | 0.2530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
