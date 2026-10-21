# EMA Hourly Continuation — DASH/USDT P26_34

**Symbol:** DASH/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 151 |
| net_profit_factor | 0.5619 |
| net_win_rate | 0.4503 |
| gross_profit_factor | 0.8166 |
| gross_win_rate | 0.4503 |
| sharpe_ratio | -2.1533 |
| sortino_ratio | -0.3785 |
| max_drawdown | 0.3791 |
| cagr | -0.1599 |
| net_avg_win | 66.8463 |
| net_avg_loss | -97.4653 |
| avg_hold_time_bars | 5.1987 |
| exposure | 0.0357 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
