# EMA Hourly Continuation — TRAC/USDT P21_34

**Symbol:** TRAC/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 935 |
| net_profit_factor | 0.3468 |
| net_win_rate | 0.4246 |
| gross_profit_factor | 0.7609 |
| gross_win_rate | 0.4439 |
| sharpe_ratio | -9.1142 |
| sortino_ratio | -3.9136 |
| max_drawdown | 0.9941 |
| cagr | -0.8678 |
| net_avg_win | 13.2907 |
| net_avg_loss | -28.2795 |
| avg_hold_time_bars | 4.1914 |
| exposure | 0.1781 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
