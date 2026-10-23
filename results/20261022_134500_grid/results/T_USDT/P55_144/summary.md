# EMA Hourly Continuation — T/USDT P55_144

**Symbol:** T/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.5179 |
| net_win_rate | 0.4491 |
| gross_profit_factor | 0.8754 |
| gross_win_rate | 0.4757 |
| sharpe_ratio | -4.2281 |
| sortino_ratio | -1.2629 |
| max_drawdown | 0.7850 |
| cagr | -0.4546 |
| net_avg_win | 41.4484 |
| net_avg_loss | -65.2486 |
| avg_hold_time_bars | 14.1504 |
| exposure | 0.2894 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
