# EMA Hourly Continuation — EGLD/USDT P34_100

**Symbol:** EGLD/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.8010 |
| net_win_rate | 0.5149 |
| gross_profit_factor | 1.0521 |
| gross_win_rate | 0.5149 |
| sharpe_ratio | -1.3433 |
| sortino_ratio | -0.3874 |
| max_drawdown | 0.4151 |
| cagr | -0.1638 |
| net_avg_win | 70.3778 |
| net_avg_loss | -93.2644 |
| avg_hold_time_bars | 15.1368 |
| exposure | 0.2766 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
