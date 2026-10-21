# EMA Hourly Continuation — RSR/USDT P26_200

**Symbol:** RSR/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.9399 |
| net_win_rate | 0.5247 |
| gross_profit_factor | 1.0946 |
| gross_win_rate | 0.5247 |
| sharpe_ratio | -0.2992 |
| sortino_ratio | -0.0776 |
| max_drawdown | 0.1437 |
| cagr | -0.0397 |
| net_avg_win | 88.9853 |
| net_avg_loss | -104.5068 |
| avg_hold_time_bars | 35.2840 |
| exposure | 0.5196 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
