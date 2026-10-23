# EMA Hourly Continuation — SQD/USDT P26_50

**Symbol:** SQD/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 867 |
| net_profit_factor | 0.6146 |
| net_win_rate | 0.4637 |
| gross_profit_factor | 0.9662 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -5.6129 |
| sortino_ratio | -2.3674 |
| max_drawdown | 0.9387 |
| cagr | -0.6795 |
| net_avg_win | 37.1648 |
| net_avg_loss | -52.2781 |
| avg_hold_time_bars | 4.1730 |
| exposure | 0.1701 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
