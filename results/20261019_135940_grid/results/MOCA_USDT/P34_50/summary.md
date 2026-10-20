# EMA Hourly Continuation — MOCA/USDT P34_50

**Symbol:** MOCA/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 831 |
| net_profit_factor | 0.3344 |
| net_win_rate | 0.4055 |
| gross_profit_factor | 0.7009 |
| gross_win_rate | 0.4356 |
| sharpe_ratio | -9.6750 |
| sortino_ratio | -4.1491 |
| max_drawdown | 0.9923 |
| cagr | -0.8802 |
| net_avg_win | 14.7889 |
| net_avg_loss | -30.1702 |
| avg_hold_time_bars | 3.0493 |
| exposure | 0.1270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
