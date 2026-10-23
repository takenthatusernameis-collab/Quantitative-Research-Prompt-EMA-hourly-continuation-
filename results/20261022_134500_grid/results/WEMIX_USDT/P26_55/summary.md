# EMA Hourly Continuation — WEMIX/USDT P26_55

**Symbol:** WEMIX/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1375 |
| net_profit_factor | 0.1545 |
| net_win_rate | 0.2676 |
| gross_profit_factor | 0.3420 |
| gross_win_rate | 0.2975 |
| sharpe_ratio | -17.8704 |
| sortino_ratio | -9.7026 |
| max_drawdown | 1.0000 |
| cagr | -0.9934 |
| net_avg_win | 4.9654 |
| net_avg_loss | -11.7450 |
| avg_hold_time_bars | 4.1571 |
| exposure | 0.2598 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
