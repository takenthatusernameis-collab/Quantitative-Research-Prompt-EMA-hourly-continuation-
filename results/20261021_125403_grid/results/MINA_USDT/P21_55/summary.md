# EMA Hourly Continuation — MINA/USDT P21_55

**Symbol:** MINA/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 549 |
| net_profit_factor | 0.7662 |
| net_win_rate | 0.5100 |
| gross_profit_factor | 1.0349 |
| gross_win_rate | 0.5100 |
| sharpe_ratio | -1.9717 |
| sortino_ratio | -0.6637 |
| max_drawdown | 0.5783 |
| cagr | -0.2626 |
| net_avg_win | 62.5726 |
| net_avg_loss | -85.0102 |
| avg_hold_time_bars | 9.1621 |
| exposure | 0.2286 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
