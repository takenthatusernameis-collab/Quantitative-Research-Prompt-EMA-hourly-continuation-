# EMA Hourly Continuation — KCS/USDT P89_100

**Symbol:** KCS/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 646 |
| net_profit_factor | 0.0470 |
| net_win_rate | 0.2353 |
| gross_profit_factor | 0.5549 |
| gross_win_rate | 0.3854 |
| sharpe_ratio | -14.5633 |
| sortino_ratio | -6.0521 |
| max_drawdown | 0.9998 |
| cagr | -0.9639 |
| net_avg_win | 3.2410 |
| net_avg_loss | -21.2353 |
| avg_hold_time_bars | 2.5635 |
| exposure | 0.0753 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
