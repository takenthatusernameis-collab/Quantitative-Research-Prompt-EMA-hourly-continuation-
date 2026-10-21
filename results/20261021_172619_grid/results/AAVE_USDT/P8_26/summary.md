# EMA Hourly Continuation — AAVE/USDT P8_26

**Symbol:** AAVE/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 601 |
| net_profit_factor | 0.7089 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.9297 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -2.7846 |
| sortino_ratio | -0.9756 |
| max_drawdown | 0.6772 |
| cagr | -0.3607 |
| net_avg_win | 57.0759 |
| net_avg_loss | -74.0786 |
| avg_hold_time_bars | 7.5940 |
| exposure | 0.2075 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
