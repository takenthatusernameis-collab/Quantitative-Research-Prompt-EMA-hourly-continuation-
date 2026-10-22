# EMA Hourly Continuation — BOSON/USDT P26_50

**Symbol:** BOSON/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 858 |
| net_profit_factor | 0.5626 |
| net_win_rate | 0.4604 |
| gross_profit_factor | 0.9408 |
| gross_win_rate | 0.4697 |
| sharpe_ratio | -5.6224 |
| sortino_ratio | -2.3209 |
| max_drawdown | 0.9389 |
| cagr | -0.6702 |
| net_avg_win | 30.5571 |
| net_avg_loss | -46.3349 |
| avg_hold_time_bars | 4.8753 |
| exposure | 0.1901 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
