# EMA Hourly Continuation — CTC/USDT P26_100

**Symbol:** CTC/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.5452 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 0.9401 |
| gross_win_rate | 0.4913 |
| sharpe_ratio | -5.0085 |
| sortino_ratio | -1.8287 |
| max_drawdown | 0.9078 |
| cagr | -0.5987 |
| net_avg_win | 33.4719 |
| net_avg_loss | -54.0112 |
| avg_hold_time_bars | 10.9186 |
| exposure | 0.3415 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
