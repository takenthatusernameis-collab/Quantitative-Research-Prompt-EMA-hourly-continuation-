# EMA Hourly Continuation — ETC/USDT P12_200

**Symbol:** ETC/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.5695 |
| net_win_rate | 0.4516 |
| gross_profit_factor | 0.8763 |
| gross_win_rate | 0.4663 |
| sharpe_ratio | -3.2565 |
| sortino_ratio | -0.8456 |
| max_drawdown | 0.6587 |
| cagr | -0.3313 |
| net_avg_win | 54.6311 |
| net_avg_loss | -79.0016 |
| avg_hold_time_bars | 48.6364 |
| exposure | 0.7539 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
