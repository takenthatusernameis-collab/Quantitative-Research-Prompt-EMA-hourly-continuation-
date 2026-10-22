# EMA Hourly Continuation — ONDO/USDT P50_89

**Symbol:** ONDO/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 691 |
| net_profit_factor | 0.4500 |
| net_win_rate | 0.4110 |
| gross_profit_factor | 0.7468 |
| gross_win_rate | 0.4211 |
| sharpe_ratio | -7.0048 |
| sortino_ratio | -2.5883 |
| max_drawdown | 0.9601 |
| cagr | -0.7208 |
| net_avg_win | 27.6416 |
| net_avg_loss | -42.8606 |
| avg_hold_time_bars | 4.6368 |
| exposure | 0.1456 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
