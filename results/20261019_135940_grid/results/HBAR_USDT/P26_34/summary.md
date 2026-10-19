# EMA Hourly Continuation — HBAR/USDT P26_34

**Symbol:** HBAR/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1026 |
| net_profit_factor | 0.2468 |
| net_win_rate | 0.3723 |
| gross_profit_factor | 0.7461 |
| gross_win_rate | 0.4142 |
| sharpe_ratio | -13.0805 |
| sortino_ratio | -6.0954 |
| max_drawdown | 0.9997 |
| cagr | -0.9614 |
| net_avg_win | 8.5735 |
| net_avg_loss | -20.6091 |
| avg_hold_time_bars | 1.9942 |
| exposure | 0.0930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
