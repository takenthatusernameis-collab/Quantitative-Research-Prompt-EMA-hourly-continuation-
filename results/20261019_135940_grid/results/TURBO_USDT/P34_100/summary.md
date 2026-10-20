# EMA Hourly Continuation — TURBO/USDT P34_100

**Symbol:** TURBO/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 573 |
| net_profit_factor | 0.7104 |
| net_win_rate | 0.4904 |
| gross_profit_factor | 1.0107 |
| gross_win_rate | 0.4939 |
| sharpe_ratio | -3.2877 |
| sortino_ratio | -1.2205 |
| max_drawdown | 0.7242 |
| cagr | -0.4371 |
| net_avg_win | 61.0637 |
| net_avg_loss | -82.7187 |
| avg_hold_time_bars | 7.9843 |
| exposure | 0.2496 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
