# EMA Hourly Continuation — VR/USDT P50_55

**Symbol:** VR/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 112 |
| net_profit_factor | 0.4147 |
| net_win_rate | 0.3571 |
| gross_profit_factor | 0.6273 |
| gross_win_rate | 0.3661 |
| sharpe_ratio | -3.0753 |
| sortino_ratio | -0.4620 |
| max_drawdown | 0.4580 |
| cagr | -0.1959 |
| net_avg_win | 74.6793 |
| net_avg_loss | -100.0480 |
| avg_hold_time_bars | 5.6339 |
| exposure | 0.0287 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
