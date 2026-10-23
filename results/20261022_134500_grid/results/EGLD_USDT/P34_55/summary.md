# EMA Hourly Continuation — EGLD/USDT P34_55

**Symbol:** EGLD/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 868 |
| net_profit_factor | 0.3533 |
| net_win_rate | 0.4389 |
| gross_profit_factor | 0.8254 |
| gross_win_rate | 0.4574 |
| sharpe_ratio | -8.4573 |
| sortino_ratio | -3.5241 |
| max_drawdown | 0.9886 |
| cagr | -0.8310 |
| net_avg_win | 14.1747 |
| net_avg_loss | -31.3871 |
| avg_hold_time_bars | 3.6083 |
| exposure | 0.1424 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
