# EMA Hourly Continuation — PROM/USDT P34_50

**Symbol:** PROM/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 930 |
| net_profit_factor | 0.3321 |
| net_win_rate | 0.3796 |
| gross_profit_factor | 0.7764 |
| gross_win_rate | 0.4280 |
| sharpe_ratio | -10.6978 |
| sortino_ratio | -4.6581 |
| max_drawdown | 0.9975 |
| cagr | -0.9085 |
| net_avg_win | 14.0532 |
| net_avg_loss | -25.8858 |
| avg_hold_time_bars | 3.1946 |
| exposure | 0.1350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
