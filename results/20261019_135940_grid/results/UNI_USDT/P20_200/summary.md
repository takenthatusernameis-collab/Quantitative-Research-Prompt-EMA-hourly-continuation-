# EMA Hourly Continuation — UNI/USDT P20_200

**Symbol:** UNI/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.6455 |
| net_win_rate | 0.4681 |
| gross_profit_factor | 0.9202 |
| gross_win_rate | 0.4787 |
| sharpe_ratio | -2.8017 |
| sortino_ratio | -0.7596 |
| max_drawdown | 0.6062 |
| cagr | -0.3073 |
| net_avg_win | 62.3271 |
| net_avg_loss | -84.9654 |
| avg_hold_time_bars | 36.7952 |
| exposure | 0.6289 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
