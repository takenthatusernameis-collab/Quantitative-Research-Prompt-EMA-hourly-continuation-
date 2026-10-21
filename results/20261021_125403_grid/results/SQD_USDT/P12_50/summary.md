# EMA Hourly Continuation — SQD/USDT P12_50

**Symbol:** SQD/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 607 |
| net_profit_factor | 0.8860 |
| net_win_rate | 0.5173 |
| gross_profit_factor | 1.0646 |
| gross_win_rate | 0.5173 |
| sharpe_ratio | -0.9326 |
| sortino_ratio | -0.3358 |
| max_drawdown | 0.3888 |
| cagr | -0.1482 |
| net_avg_win | 79.8465 |
| net_avg_loss | -96.5788 |
| avg_hold_time_bars | 10.5766 |
| exposure | 0.3018 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
