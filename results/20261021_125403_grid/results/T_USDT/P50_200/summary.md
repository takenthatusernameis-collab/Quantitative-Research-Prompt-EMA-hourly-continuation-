# EMA Hourly Continuation — T/USDT P50_200

**Symbol:** T/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 296 |
| net_profit_factor | 0.7340 |
| net_win_rate | 0.4966 |
| gross_profit_factor | 0.9843 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.5614 |
| sortino_ratio | -0.3834 |
| max_drawdown | 0.3713 |
| cagr | -0.1607 |
| net_avg_win | 67.0441 |
| net_avg_loss | -90.1201 |
| avg_hold_time_bars | 30.1622 |
| exposure | 0.4040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
