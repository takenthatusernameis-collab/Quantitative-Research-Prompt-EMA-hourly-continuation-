# EMA Hourly Continuation — XPR/USDT P8_34

**Symbol:** XPR/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1356 |
| net_profit_factor | 0.3833 |
| net_win_rate | 0.4034 |
| gross_profit_factor | 0.7428 |
| gross_win_rate | 0.4152 |
| sharpe_ratio | -11.9688 |
| sortino_ratio | -6.1912 |
| max_drawdown | 0.9997 |
| cagr | -0.9607 |
| net_avg_win | 11.3592 |
| net_avg_loss | -20.0377 |
| avg_hold_time_bars | 5.0324 |
| exposure | 0.3102 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
