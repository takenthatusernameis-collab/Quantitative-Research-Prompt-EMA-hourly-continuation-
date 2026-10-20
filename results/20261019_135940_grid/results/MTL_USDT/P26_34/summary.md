# EMA Hourly Continuation — MTL/USDT P26_34

**Symbol:** MTL/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1059 |
| net_profit_factor | 0.2726 |
| net_win_rate | 0.3626 |
| gross_profit_factor | 0.7657 |
| gross_win_rate | 0.4174 |
| sharpe_ratio | -13.2787 |
| sortino_ratio | -6.2502 |
| max_drawdown | 0.9998 |
| cagr | -0.9635 |
| net_avg_win | 9.7554 |
| net_avg_loss | -20.3610 |
| avg_hold_time_bars | 3.0633 |
| exposure | 0.1468 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
