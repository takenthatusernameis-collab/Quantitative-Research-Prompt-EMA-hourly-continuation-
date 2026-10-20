# EMA Hourly Continuation — FIDA/USDT P89_100

**Symbol:** FIDA/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 606 |
| net_profit_factor | 0.2686 |
| net_win_rate | 0.3927 |
| gross_profit_factor | 0.6948 |
| gross_win_rate | 0.4323 |
| sharpe_ratio | -8.4561 |
| sortino_ratio | -2.9850 |
| max_drawdown | 0.9781 |
| cagr | -0.7795 |
| net_avg_win | 15.0900 |
| net_avg_loss | -36.3338 |
| avg_hold_time_bars | 3.4241 |
| exposure | 0.0939 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
