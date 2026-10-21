# EMA Hourly Continuation — XPR/USDT P34_50

**Symbol:** XPR/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 142 |
| net_profit_factor | 0.8437 |
| net_win_rate | 0.5423 |
| gross_profit_factor | 1.1795 |
| gross_win_rate | 0.5423 |
| sharpe_ratio | -0.6232 |
| sortino_ratio | -0.1076 |
| max_drawdown | 0.1764 |
| cagr | -0.0488 |
| net_avg_win | 82.7306 |
| net_avg_loss | -116.1558 |
| avg_hold_time_bars | 13.4366 |
| exposure | 0.0867 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
