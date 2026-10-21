# EMA Hourly Continuation — XNO/USDT P21_34

**Symbol:** XNO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.5477 |
| net_win_rate | 0.4140 |
| gross_profit_factor | 0.7703 |
| gross_win_rate | 0.4140 |
| sharpe_ratio | -3.7423 |
| sortino_ratio | -0.9434 |
| max_drawdown | 0.6786 |
| cagr | -0.3537 |
| net_avg_win | 62.0333 |
| net_avg_loss | -80.0161 |
| avg_hold_time_bars | 4.9427 |
| exposure | 0.0705 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
