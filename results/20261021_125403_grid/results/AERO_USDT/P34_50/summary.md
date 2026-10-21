# EMA Hourly Continuation — AERO/USDT P34_50

**Symbol:** AERO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 222 |
| net_profit_factor | 0.7700 |
| net_win_rate | 0.5045 |
| gross_profit_factor | 1.0170 |
| gross_win_rate | 0.5045 |
| sharpe_ratio | -1.2250 |
| sortino_ratio | -0.2617 |
| max_drawdown | 0.2824 |
| cagr | -0.1140 |
| net_avg_win | 78.3329 |
| net_avg_loss | -103.5786 |
| avg_hold_time_bars | 5.8694 |
| exposure | 0.0592 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
