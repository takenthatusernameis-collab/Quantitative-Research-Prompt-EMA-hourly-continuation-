# EMA Hourly Continuation — ZBCN/USDT P12_200

**Symbol:** ZBCN/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 1.1109 |
| net_win_rate | 0.5635 |
| gross_profit_factor | 1.2588 |
| gross_win_rate | 0.5635 |
| sharpe_ratio | 0.8271 |
| sortino_ratio | 0.2486 |
| max_drawdown | 0.1998 |
| cagr | 0.1039 |
| net_avg_win | 117.7531 |
| net_avg_loss | -136.8667 |
| avg_hold_time_bars | 34.3669 |
| exposure | 0.6630 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
