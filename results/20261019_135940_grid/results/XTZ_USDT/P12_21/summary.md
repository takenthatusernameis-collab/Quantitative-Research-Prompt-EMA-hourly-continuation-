# EMA Hourly Continuation — XTZ/USDT P12_21

**Symbol:** XTZ/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1484 |
| net_profit_factor | 0.2470 |
| net_win_rate | 0.3888 |
| gross_profit_factor | 0.8260 |
| gross_win_rate | 0.4508 |
| sharpe_ratio | -14.5619 |
| sortino_ratio | -8.0706 |
| max_drawdown | 1.0000 |
| cagr | -0.9850 |
| net_avg_win | 5.6842 |
| net_avg_loss | -14.6412 |
| avg_hold_time_bars | 2.3497 |
| exposure | 0.1585 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
