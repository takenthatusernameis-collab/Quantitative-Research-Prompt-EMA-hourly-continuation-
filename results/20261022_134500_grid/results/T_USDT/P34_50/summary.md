# EMA Hourly Continuation — T/USDT P34_50

**Symbol:** T/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 765 |
| net_profit_factor | 0.3725 |
| net_win_rate | 0.4222 |
| gross_profit_factor | 0.8259 |
| gross_win_rate | 0.4471 |
| sharpe_ratio | -8.6509 |
| sortino_ratio | -3.3934 |
| max_drawdown | 0.9874 |
| cagr | -0.8217 |
| net_avg_win | 18.1382 |
| net_avg_loss | -35.5870 |
| avg_hold_time_bars | 4.3320 |
| exposure | 0.1500 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
