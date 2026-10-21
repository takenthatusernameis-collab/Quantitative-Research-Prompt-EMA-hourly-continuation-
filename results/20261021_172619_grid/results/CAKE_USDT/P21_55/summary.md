# EMA Hourly Continuation — CAKE/USDT P21_55

**Symbol:** CAKE/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.6416 |
| net_win_rate | 0.4760 |
| gross_profit_factor | 0.8998 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -3.0650 |
| sortino_ratio | -0.9799 |
| max_drawdown | 0.6803 |
| cagr | -0.3627 |
| net_avg_win | 50.9499 |
| net_avg_loss | -72.1365 |
| avg_hold_time_bars | 9.6040 |
| exposure | 0.2183 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
