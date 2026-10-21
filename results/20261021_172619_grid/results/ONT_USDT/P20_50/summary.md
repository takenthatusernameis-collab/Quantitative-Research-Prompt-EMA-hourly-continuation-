# EMA Hourly Continuation — ONT/USDT P20_50

**Symbol:** ONT/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 512 |
| net_profit_factor | 0.7804 |
| net_win_rate | 0.5117 |
| gross_profit_factor | 1.0691 |
| gross_win_rate | 0.5117 |
| sharpe_ratio | -1.9473 |
| sortino_ratio | -0.6319 |
| max_drawdown | 0.5570 |
| cagr | -0.2523 |
| net_avg_win | 70.5105 |
| net_avg_loss | -94.6847 |
| avg_hold_time_bars | 7.3379 |
| exposure | 0.1700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
