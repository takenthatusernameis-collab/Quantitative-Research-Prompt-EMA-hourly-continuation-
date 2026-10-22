# EMA Hourly Continuation — EGLD/USDT P21_89

**Symbol:** EGLD/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 702 |
| net_profit_factor | 0.5861 |
| net_win_rate | 0.4744 |
| gross_profit_factor | 0.9397 |
| gross_win_rate | 0.4801 |
| sharpe_ratio | -4.5265 |
| sortino_ratio | -1.6789 |
| max_drawdown | 0.8812 |
| cagr | -0.5604 |
| net_avg_win | 37.1188 |
| net_avg_loss | -57.1576 |
| avg_hold_time_bars | 12.3732 |
| exposure | 0.3948 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
