# EMA Hourly Continuation — ORCA/USDT P12_20

**Symbol:** ORCA/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.7156 |
| net_win_rate | 0.5154 |
| gross_profit_factor | 1.0863 |
| gross_win_rate | 0.5197 |
| sharpe_ratio | -2.3646 |
| sortino_ratio | -0.7247 |
| max_drawdown | 0.6037 |
| cagr | -0.2845 |
| net_avg_win | 60.8832 |
| net_avg_loss | -90.4664 |
| avg_hold_time_bars | 5.3004 |
| exposure | 0.1099 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
