# EMA Hourly Continuation — ICP/USDT P21_50

**Symbol:** ICP/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1013 |
| net_profit_factor | 0.4686 |
| net_win_rate | 0.4501 |
| gross_profit_factor | 0.8727 |
| gross_win_rate | 0.4669 |
| sharpe_ratio | -7.7006 |
| sortino_ratio | -3.4412 |
| max_drawdown | 0.9868 |
| cagr | -0.8188 |
| net_avg_win | 19.0767 |
| net_avg_loss | -33.3249 |
| avg_hold_time_bars | 4.4413 |
| exposure | 0.2045 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
