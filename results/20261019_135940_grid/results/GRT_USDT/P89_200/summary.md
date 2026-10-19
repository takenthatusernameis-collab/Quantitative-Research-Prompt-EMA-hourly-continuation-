# EMA Hourly Continuation — GRT/USDT P89_200

**Symbol:** GRT/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.5537 |
| net_win_rate | 0.4808 |
| gross_profit_factor | 0.9385 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -3.6500 |
| sortino_ratio | -1.0065 |
| max_drawdown | 0.7280 |
| cagr | -0.3928 |
| net_avg_win | 47.2350 |
| net_avg_loss | -79.0114 |
| avg_hold_time_bars | 9.9309 |
| exposure | 0.1757 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
