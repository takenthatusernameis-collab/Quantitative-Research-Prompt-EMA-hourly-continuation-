# EMA Hourly Continuation — SHIB/USDT P12_34

**Symbol:** SHIB/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1323 |
| net_profit_factor | 0.3867 |
| net_win_rate | 0.4429 |
| gross_profit_factor | 0.8415 |
| gross_win_rate | 0.4649 |
| sharpe_ratio | -10.4758 |
| sortino_ratio | -5.3767 |
| max_drawdown | 0.9990 |
| cagr | -0.9354 |
| net_avg_win | 10.7480 |
| net_avg_loss | -22.1004 |
| avg_hold_time_bars | 3.7370 |
| exposure | 0.2247 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
