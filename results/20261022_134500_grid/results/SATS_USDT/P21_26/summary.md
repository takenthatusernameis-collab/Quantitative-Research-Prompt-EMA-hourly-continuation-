# EMA Hourly Continuation — SATS/USDT P21_26

**Symbol:** SATS/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 885 |
| net_profit_factor | 0.3491 |
| net_win_rate | 0.4271 |
| gross_profit_factor | 0.8865 |
| gross_win_rate | 0.4463 |
| sharpe_ratio | -8.9078 |
| sortino_ratio | -3.7347 |
| max_drawdown | 0.9922 |
| cagr | -0.8532 |
| net_avg_win | 14.0781 |
| net_avg_loss | -30.0641 |
| avg_hold_time_bars | 2.3243 |
| exposure | 0.0931 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
