# EMA Hourly Continuation — IMX/USDT P21_55

**Symbol:** IMX/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 927 |
| net_profit_factor | 0.5231 |
| net_win_rate | 0.4639 |
| gross_profit_factor | 0.8759 |
| gross_win_rate | 0.4757 |
| sharpe_ratio | -5.8465 |
| sortino_ratio | -2.4778 |
| max_drawdown | 0.9552 |
| cagr | -0.7056 |
| net_avg_win | 24.3432 |
| net_avg_loss | -40.2620 |
| avg_hold_time_bars | 5.5146 |
| exposure | 0.2313 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
