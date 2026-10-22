# EMA Hourly Continuation — MLK/USDT P21_26

**Symbol:** MLK/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 231 |
| net_profit_factor | 0.2513 |
| net_win_rate | 0.2857 |
| gross_profit_factor | 0.4181 |
| gross_win_rate | 0.2900 |
| sharpe_ratio | -6.0168 |
| sortino_ratio | -1.3090 |
| max_drawdown | 0.8004 |
| cagr | -0.4687 |
| net_avg_win | 40.5315 |
| net_avg_loss | -64.5231 |
| avg_hold_time_bars | 5.3723 |
| exposure | 0.0562 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
