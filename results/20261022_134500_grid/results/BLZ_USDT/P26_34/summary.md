# EMA Hourly Continuation — BLZ/USDT P26_34

**Symbol:** BLZ/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1112 |
| net_profit_factor | 0.2489 |
| net_win_rate | 0.3282 |
| gross_profit_factor | 0.6712 |
| gross_win_rate | 0.3777 |
| sharpe_ratio | -13.9480 |
| sortino_ratio | -6.7300 |
| max_drawdown | 0.9998 |
| cagr | -0.9686 |
| net_avg_win | 9.0791 |
| net_avg_loss | -17.8210 |
| avg_hold_time_bars | 2.9649 |
| exposure | 0.1492 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
