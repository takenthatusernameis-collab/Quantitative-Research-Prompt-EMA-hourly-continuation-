# EMA Hourly Continuation — BIGTIME/USDT P34_55

**Symbol:** BIGTIME/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 861 |
| net_profit_factor | 0.5356 |
| net_win_rate | 0.4727 |
| gross_profit_factor | 0.9334 |
| gross_win_rate | 0.4890 |
| sharpe_ratio | -6.0380 |
| sortino_ratio | -2.5029 |
| max_drawdown | 0.9534 |
| cagr | -0.7003 |
| net_avg_win | 26.9753 |
| net_avg_loss | -45.1547 |
| avg_hold_time_bars | 3.7666 |
| exposure | 0.1468 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
