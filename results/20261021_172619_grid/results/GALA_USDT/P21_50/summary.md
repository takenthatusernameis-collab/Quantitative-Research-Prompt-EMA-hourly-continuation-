# EMA Hourly Continuation — GALA/USDT P21_50

**Symbol:** GALA/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.6788 |
| net_win_rate | 0.4661 |
| gross_profit_factor | 0.8854 |
| gross_win_rate | 0.4661 |
| sharpe_ratio | -2.8271 |
| sortino_ratio | -0.8896 |
| max_drawdown | 0.6657 |
| cagr | -0.3349 |
| net_avg_win | 59.6818 |
| net_avg_loss | -76.7575 |
| avg_hold_time_bars | 6.6242 |
| exposure | 0.1466 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
