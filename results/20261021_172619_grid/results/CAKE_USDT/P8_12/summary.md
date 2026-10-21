# EMA Hourly Continuation — CAKE/USDT P8_12

**Symbol:** CAKE/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 235 |
| net_profit_factor | 0.7655 |
| net_win_rate | 0.5404 |
| gross_profit_factor | 1.1713 |
| gross_win_rate | 0.5404 |
| sharpe_ratio | -1.2510 |
| sortino_ratio | -0.2781 |
| max_drawdown | 0.2900 |
| cagr | -0.1190 |
| net_avg_win | 70.0656 |
| net_avg_loss | -107.6265 |
| avg_hold_time_bars | 5.0043 |
| exposure | 0.0535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
