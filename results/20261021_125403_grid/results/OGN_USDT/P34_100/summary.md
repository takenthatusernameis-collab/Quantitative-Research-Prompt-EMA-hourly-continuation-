# EMA Hourly Continuation — OGN/USDT P34_100

**Symbol:** OGN/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.6727 |
| net_win_rate | 0.4708 |
| gross_profit_factor | 0.9099 |
| gross_win_rate | 0.4708 |
| sharpe_ratio | -2.9374 |
| sortino_ratio | -0.8988 |
| max_drawdown | 0.6619 |
| cagr | -0.3379 |
| net_avg_win | 60.9635 |
| net_avg_loss | -80.6356 |
| avg_hold_time_bars | 13.1598 |
| exposure | 0.2757 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
