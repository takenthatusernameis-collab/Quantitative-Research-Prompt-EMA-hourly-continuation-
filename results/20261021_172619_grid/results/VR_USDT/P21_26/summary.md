# EMA Hourly Continuation — VR/USDT P21_26

**Symbol:** VR/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 163 |
| net_profit_factor | 0.5332 |
| net_win_rate | 0.4049 |
| gross_profit_factor | 0.8117 |
| gross_win_rate | 0.4294 |
| sharpe_ratio | -2.7758 |
| sortino_ratio | -0.5018 |
| max_drawdown | 0.4581 |
| cagr | -0.2107 |
| net_avg_win | 77.5381 |
| net_avg_loss | -98.9465 |
| avg_hold_time_bars | 6.8282 |
| exposure | 0.0506 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
