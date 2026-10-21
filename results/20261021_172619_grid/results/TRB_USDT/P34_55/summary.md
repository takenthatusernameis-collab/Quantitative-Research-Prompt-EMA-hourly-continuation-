# EMA Hourly Continuation — TRB/USDT P34_55

**Symbol:** TRB/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.6445 |
| net_win_rate | 0.4602 |
| gross_profit_factor | 0.8993 |
| gross_win_rate | 0.4602 |
| sharpe_ratio | -2.9289 |
| sortino_ratio | -0.7690 |
| max_drawdown | 0.6365 |
| cagr | -0.2982 |
| net_avg_win | 68.6275 |
| net_avg_loss | -90.7772 |
| avg_hold_time_bars | 5.0177 |
| exposure | 0.0770 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
