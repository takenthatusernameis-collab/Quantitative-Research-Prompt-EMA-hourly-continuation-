# EMA Hourly Continuation — JUP/USDT P20_50

**Symbol:** JUP/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.8007 |
| net_win_rate | 0.5052 |
| gross_profit_factor | 1.0176 |
| gross_win_rate | 0.5052 |
| sharpe_ratio | -1.5419 |
| sortino_ratio | -0.4874 |
| max_drawdown | 0.4734 |
| cagr | -0.2011 |
| net_avg_win | 70.6593 |
| net_avg_loss | -90.0890 |
| avg_hold_time_bars | 7.7753 |
| exposure | 0.1714 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
