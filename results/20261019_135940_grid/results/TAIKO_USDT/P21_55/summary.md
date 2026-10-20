# EMA Hourly Continuation — TAIKO/USDT P21_55

**Symbol:** TAIKO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 825 |
| net_profit_factor | 0.5368 |
| net_win_rate | 0.4679 |
| gross_profit_factor | 0.9046 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -6.1527 |
| sortino_ratio | -2.5544 |
| max_drawdown | 0.9534 |
| cagr | -0.7137 |
| net_avg_win | 28.4895 |
| net_avg_loss | -46.6626 |
| avg_hold_time_bars | 6.0509 |
| exposure | 0.2398 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
