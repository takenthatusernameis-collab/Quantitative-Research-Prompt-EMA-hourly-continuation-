# EMA Hourly Continuation — API3/USDT P100_200

**Symbol:** API3/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.7346 |
| net_win_rate | 0.5064 |
| gross_profit_factor | 1.0718 |
| gross_win_rate | 0.5140 |
| sharpe_ratio | -2.0540 |
| sortino_ratio | -0.5791 |
| max_drawdown | 0.5180 |
| cagr | -0.2382 |
| net_avg_win | 68.8544 |
| net_avg_loss | -96.1502 |
| avg_hold_time_bars | 9.9033 |
| exposure | 0.1769 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
