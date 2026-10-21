# EMA Hourly Continuation — METIS/USDT P21_26

**Symbol:** METIS/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 198 |
| net_profit_factor | 0.6504 |
| net_win_rate | 0.4798 |
| gross_profit_factor | 0.9372 |
| gross_win_rate | 0.4798 |
| sharpe_ratio | -1.9913 |
| sortino_ratio | -0.4015 |
| max_drawdown | 0.3979 |
| cagr | -0.1688 |
| net_avg_win | 72.7322 |
| net_avg_loss | -103.1460 |
| avg_hold_time_bars | 4.3384 |
| exposure | 0.0390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
