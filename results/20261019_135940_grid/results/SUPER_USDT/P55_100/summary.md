# EMA Hourly Continuation — SUPER/USDT P55_100

**Symbol:** SUPER/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 580 |
| net_profit_factor | 0.5735 |
| net_win_rate | 0.4914 |
| gross_profit_factor | 0.9226 |
| gross_win_rate | 0.4983 |
| sharpe_ratio | -3.7639 |
| sortino_ratio | -1.2823 |
| max_drawdown | 0.7949 |
| cagr | -0.4567 |
| net_avg_win | 36.9898 |
| net_avg_loss | -62.3113 |
| avg_hold_time_bars | 6.3086 |
| exposure | 0.1663 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
