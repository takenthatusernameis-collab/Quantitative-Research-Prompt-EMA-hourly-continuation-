# EMA Hourly Continuation — SLP/USDT P20_100

**Symbol:** SLP/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 743 |
| net_profit_factor | 0.6109 |
| net_win_rate | 0.4563 |
| gross_profit_factor | 0.9418 |
| gross_win_rate | 0.4630 |
| sharpe_ratio | -5.0806 |
| sortino_ratio | -1.9380 |
| max_drawdown | 0.9096 |
| cagr | -0.6106 |
| net_avg_win | 41.9852 |
| net_avg_loss | -57.6648 |
| avg_hold_time_bars | 13.6083 |
| exposure | 0.4596 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
