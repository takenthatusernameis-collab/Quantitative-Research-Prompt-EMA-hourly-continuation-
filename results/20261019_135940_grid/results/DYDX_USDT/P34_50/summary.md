# EMA Hourly Continuation — DYDX/USDT P34_50

**Symbol:** DYDX/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 952 |
| net_profit_factor | 0.3970 |
| net_win_rate | 0.4391 |
| gross_profit_factor | 0.8687 |
| gross_win_rate | 0.4622 |
| sharpe_ratio | -8.5736 |
| sortino_ratio | -3.7578 |
| max_drawdown | 0.9912 |
| cagr | -0.8449 |
| net_avg_win | 15.6014 |
| net_avg_loss | -30.7651 |
| avg_hold_time_bars | 2.6765 |
| exposure | 0.1158 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
