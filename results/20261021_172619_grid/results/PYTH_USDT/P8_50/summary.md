# EMA Hourly Continuation — PYTH/USDT P8_50

**Symbol:** PYTH/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 692 |
| net_profit_factor | 0.8105 |
| net_win_rate | 0.4870 |
| gross_profit_factor | 0.9843 |
| gross_win_rate | 0.4870 |
| sharpe_ratio | -2.0873 |
| sortino_ratio | -0.7835 |
| max_drawdown | 0.6715 |
| cagr | -0.3038 |
| net_avg_win | 75.7978 |
| net_avg_loss | -88.7790 |
| avg_hold_time_bars | 12.9552 |
| exposure | 0.4075 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
