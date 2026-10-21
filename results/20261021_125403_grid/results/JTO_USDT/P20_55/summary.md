# EMA Hourly Continuation — JTO/USDT P20_55

**Symbol:** JTO/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 577 |
| net_profit_factor | 0.7643 |
| net_win_rate | 0.4818 |
| gross_profit_factor | 0.9540 |
| gross_win_rate | 0.4818 |
| sharpe_ratio | -2.2294 |
| sortino_ratio | -0.7643 |
| max_drawdown | 0.6081 |
| cagr | -0.2971 |
| net_avg_win | 68.5324 |
| net_avg_loss | -83.3641 |
| avg_hold_time_bars | 8.9913 |
| exposure | 0.2358 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
