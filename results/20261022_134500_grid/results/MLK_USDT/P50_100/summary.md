# EMA Hourly Continuation — MLK/USDT P50_100

**Symbol:** MLK/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 876 |
| net_profit_factor | 0.2261 |
| net_win_rate | 0.2717 |
| gross_profit_factor | 0.4787 |
| gross_win_rate | 0.2808 |
| sharpe_ratio | -13.4508 |
| sortino_ratio | -5.7219 |
| max_drawdown | 0.9995 |
| cagr | -0.9494 |
| net_avg_win | 12.2712 |
| net_avg_loss | -20.2432 |
| avg_hold_time_bars | 4.9144 |
| exposure | 0.1948 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
