# EMA Hourly Continuation — CETUS/USDT P12_50

**Symbol:** CETUS/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1091 |
| net_profit_factor | 0.6528 |
| net_win_rate | 0.4629 |
| gross_profit_factor | 1.0154 |
| gross_win_rate | 0.4775 |
| sharpe_ratio | -6.0050 |
| sortino_ratio | -2.7762 |
| max_drawdown | 0.9691 |
| cagr | -0.7387 |
| net_avg_win | 35.9658 |
| net_avg_loss | -47.4813 |
| avg_hold_time_bars | 7.1366 |
| exposure | 0.3523 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
