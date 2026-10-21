# EMA Hourly Continuation — CKB/USDT P34_55

**Symbol:** CKB/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.6307 |
| net_win_rate | 0.4754 |
| gross_profit_factor | 0.8995 |
| gross_win_rate | 0.4754 |
| sharpe_ratio | -2.7364 |
| sortino_ratio | -0.7274 |
| max_drawdown | 0.5698 |
| cagr | -0.2832 |
| net_avg_win | 59.0113 |
| net_avg_loss | -84.7759 |
| avg_hold_time_bars | 4.9246 |
| exposure | 0.0772 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
