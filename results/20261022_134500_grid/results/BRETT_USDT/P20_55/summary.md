# EMA Hourly Continuation — BRETT/USDT P20_55

**Symbol:** BRETT/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 918 |
| net_profit_factor | 0.5940 |
| net_win_rate | 0.4466 |
| gross_profit_factor | 0.8881 |
| gross_win_rate | 0.4542 |
| sharpe_ratio | -6.0071 |
| sortino_ratio | -2.6189 |
| max_drawdown | 0.9518 |
| cagr | -0.7210 |
| net_avg_win | 33.9632 |
| net_avg_loss | -46.1438 |
| avg_hold_time_bars | 5.2495 |
| exposure | 0.2319 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
