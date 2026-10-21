# EMA Hourly Continuation — CAKE/USDT P21_50

**Symbol:** CAKE/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.6231 |
| net_win_rate | 0.4763 |
| gross_profit_factor | 0.8854 |
| gross_win_rate | 0.4763 |
| sharpe_ratio | -3.0854 |
| sortino_ratio | -0.9724 |
| max_drawdown | 0.6795 |
| cagr | -0.3602 |
| net_avg_win | 48.2601 |
| net_avg_loss | -70.4343 |
| avg_hold_time_bars | 8.7031 |
| exposure | 0.1919 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
