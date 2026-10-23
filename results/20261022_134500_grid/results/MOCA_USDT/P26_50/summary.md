# EMA Hourly Continuation — MOCA/USDT P26_50

**Symbol:** MOCA/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 843 |
| net_profit_factor | 0.4341 |
| net_win_rate | 0.4318 |
| gross_profit_factor | 0.8214 |
| gross_win_rate | 0.4543 |
| sharpe_ratio | -7.9147 |
| sortino_ratio | -3.3973 |
| max_drawdown | 0.9789 |
| cagr | -0.8143 |
| net_avg_win | 20.6219 |
| net_avg_loss | -36.0960 |
| avg_hold_time_bars | 3.8422 |
| exposure | 0.1624 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
