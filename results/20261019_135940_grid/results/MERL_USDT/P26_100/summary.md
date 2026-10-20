# EMA Hourly Continuation — MERL/USDT P26_100

**Symbol:** MERL/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 656 |
| net_profit_factor | 0.6426 |
| net_win_rate | 0.4649 |
| gross_profit_factor | 0.8694 |
| gross_win_rate | 0.4649 |
| sharpe_ratio | -3.5254 |
| sortino_ratio | -1.2737 |
| max_drawdown | 0.7879 |
| cagr | -0.4515 |
| net_avg_win | 45.8399 |
| net_avg_loss | -61.9896 |
| avg_hold_time_bars | 11.6601 |
| exposure | 0.3486 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
