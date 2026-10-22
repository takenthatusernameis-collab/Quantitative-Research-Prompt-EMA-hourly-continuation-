# EMA Hourly Continuation — PYTH/USDT P50_100

**Symbol:** PYTH/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 649 |
| net_profit_factor | 0.5172 |
| net_win_rate | 0.4622 |
| gross_profit_factor | 0.8571 |
| gross_win_rate | 0.4684 |
| sharpe_ratio | -4.9137 |
| sortino_ratio | -1.7594 |
| max_drawdown | 0.8856 |
| cagr | -0.5723 |
| net_avg_win | 31.4767 |
| net_avg_loss | -52.3150 |
| avg_hold_time_bars | 5.4869 |
| exposure | 0.1619 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
