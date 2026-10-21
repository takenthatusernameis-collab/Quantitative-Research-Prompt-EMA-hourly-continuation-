# EMA Hourly Continuation — ORBS/USDT P12_100

**Symbol:** ORBS/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 579 |
| net_profit_factor | 0.6746 |
| net_win_rate | 0.4542 |
| gross_profit_factor | 0.8865 |
| gross_win_rate | 0.4560 |
| sharpe_ratio | -3.5385 |
| sortino_ratio | -1.2086 |
| max_drawdown | 0.7642 |
| cagr | -0.4280 |
| net_avg_win | 59.4590 |
| net_avg_loss | -73.3521 |
| avg_hold_time_bars | 20.4750 |
| exposure | 0.5389 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
