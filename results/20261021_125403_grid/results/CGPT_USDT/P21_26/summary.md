# EMA Hourly Continuation — CGPT/USDT P21_26

**Symbol:** CGPT/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 167 |
| net_profit_factor | 0.6285 |
| net_win_rate | 0.4671 |
| gross_profit_factor | 0.8600 |
| gross_win_rate | 0.4671 |
| sharpe_ratio | -1.8139 |
| sortino_ratio | -0.3349 |
| max_drawdown | 0.3469 |
| cagr | -0.1420 |
| net_avg_win | 69.2679 |
| net_avg_loss | -96.5880 |
| avg_hold_time_bars | 5.0479 |
| exposure | 0.0383 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
