# EMA Hourly Continuation — OP/USDT P26_50

**Symbol:** OP/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.7389 |
| net_win_rate | 0.5073 |
| gross_profit_factor | 0.9996 |
| gross_win_rate | 0.5073 |
| sharpe_ratio | -1.7313 |
| sortino_ratio | -0.5037 |
| max_drawdown | 0.4674 |
| cagr | -0.2059 |
| net_avg_win | 59.7818 |
| net_avg_loss | -83.3130 |
| avg_hold_time_bars | 5.5537 |
| exposure | 0.1035 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
