# EMA Hourly Continuation — EGLD/USDT P12_50

**Symbol:** EGLD/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 679 |
| net_profit_factor | 0.7237 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 0.9678 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -2.9642 |
| sortino_ratio | -1.1044 |
| max_drawdown | 0.7378 |
| cagr | -0.3976 |
| net_avg_win | 57.4971 |
| net_avg_loss | -74.2413 |
| avg_hold_time_bars | 10.2091 |
| exposure | 0.3151 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
