# EMA Hourly Continuation — EDU/USDT P50_200

**Symbol:** EDU/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.7252 |
| net_win_rate | 0.4645 |
| gross_profit_factor | 0.8638 |
| gross_win_rate | 0.4645 |
| sharpe_ratio | -1.7625 |
| sortino_ratio | -0.4395 |
| max_drawdown | 0.4460 |
| cagr | -0.1842 |
| net_avg_win | 73.6016 |
| net_avg_loss | -88.0376 |
| avg_hold_time_bars | 29.6548 |
| exposure | 0.4160 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
