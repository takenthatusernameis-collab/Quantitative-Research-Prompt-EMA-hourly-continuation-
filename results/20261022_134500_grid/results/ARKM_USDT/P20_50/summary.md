# EMA Hourly Continuation — ARKM/USDT P20_50

**Symbol:** ARKM/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1038 |
| net_profit_factor | 0.5794 |
| net_win_rate | 0.4441 |
| gross_profit_factor | 0.9244 |
| gross_win_rate | 0.4538 |
| sharpe_ratio | -6.9421 |
| sortino_ratio | -3.1535 |
| max_drawdown | 0.9783 |
| cagr | -0.7807 |
| net_avg_win | 29.2181 |
| net_avg_loss | -40.2913 |
| avg_hold_time_bars | 4.5674 |
| exposure | 0.2155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
