# EMA Hourly Continuation — SUSHI/USDT P21_26

**Symbol:** SUSHI/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 202 |
| net_profit_factor | 0.5885 |
| net_win_rate | 0.4554 |
| gross_profit_factor | 0.8539 |
| gross_win_rate | 0.4554 |
| sharpe_ratio | -2.4560 |
| sortino_ratio | -0.4984 |
| max_drawdown | 0.4486 |
| cagr | -0.2054 |
| net_avg_win | 68.4143 |
| net_avg_loss | -97.2302 |
| avg_hold_time_bars | 4.0891 |
| exposure | 0.0374 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
