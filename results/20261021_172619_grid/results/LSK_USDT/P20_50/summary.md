# EMA Hourly Continuation — LSK/USDT P20_50

**Symbol:** LSK/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 565 |
| net_profit_factor | 0.6480 |
| net_win_rate | 0.4796 |
| gross_profit_factor | 0.9359 |
| gross_win_rate | 0.4796 |
| sharpe_ratio | -3.3295 |
| sortino_ratio | -1.1325 |
| max_drawdown | 0.7356 |
| cagr | -0.4033 |
| net_avg_win | 49.3601 |
| net_avg_loss | -70.2128 |
| avg_hold_time_bars | 8.3115 |
| exposure | 0.2135 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
