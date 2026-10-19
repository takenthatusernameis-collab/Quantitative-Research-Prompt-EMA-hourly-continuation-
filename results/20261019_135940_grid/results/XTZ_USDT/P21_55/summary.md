# EMA Hourly Continuation — XTZ/USDT P21_55

**Symbol:** XTZ/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1005 |
| net_profit_factor | 0.4728 |
| net_win_rate | 0.4498 |
| gross_profit_factor | 0.9471 |
| gross_win_rate | 0.4687 |
| sharpe_ratio | -8.0484 |
| sortino_ratio | -3.5911 |
| max_drawdown | 0.9891 |
| cagr | -0.8324 |
| net_avg_win | 19.6205 |
| net_avg_loss | -33.9164 |
| avg_hold_time_bars | 5.4458 |
| exposure | 0.2488 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
