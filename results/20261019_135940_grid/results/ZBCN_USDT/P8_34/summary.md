# EMA Hourly Continuation — ZBCN/USDT P8_34

**Symbol:** ZBCN/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1531 |
| net_profit_factor | 0.5554 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 0.8790 |
| gross_win_rate | 0.4886 |
| sharpe_ratio | -6.2747 |
| sortino_ratio | -3.4690 |
| max_drawdown | 0.9853 |
| cagr | -0.8159 |
| net_avg_win | 16.5781 |
| net_avg_loss | -28.0700 |
| avg_hold_time_bars | 4.5754 |
| exposure | 0.3241 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
