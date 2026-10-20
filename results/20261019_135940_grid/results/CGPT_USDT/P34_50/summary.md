# EMA Hourly Continuation — CGPT/USDT P34_50

**Symbol:** CGPT/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 860 |
| net_profit_factor | 0.3359 |
| net_win_rate | 0.3930 |
| gross_profit_factor | 0.7488 |
| gross_win_rate | 0.4209 |
| sharpe_ratio | -9.4541 |
| sortino_ratio | -3.9375 |
| max_drawdown | 0.9934 |
| cagr | -0.8648 |
| net_avg_win | 14.8690 |
| net_avg_loss | -28.6590 |
| avg_hold_time_bars | 2.9000 |
| exposure | 0.1134 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
