# EMA Hourly Continuation — COMP/USDT P50_55

**Symbol:** COMP/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 891 |
| net_profit_factor | 0.1551 |
| net_win_rate | 0.3580 |
| gross_profit_factor | 0.6676 |
| gross_win_rate | 0.4456 |
| sharpe_ratio | -12.7792 |
| sortino_ratio | -5.6347 |
| max_drawdown | 0.9995 |
| cagr | -0.9501 |
| net_avg_win | 5.7531 |
| net_avg_loss | -20.6816 |
| avg_hold_time_bars | 2.0988 |
| exposure | 0.0850 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
