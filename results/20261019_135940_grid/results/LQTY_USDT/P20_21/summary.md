# EMA Hourly Continuation — LQTY/USDT P20_21

**Symbol:** LQTY/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1267 |
| net_profit_factor | 0.1628 |
| net_win_rate | 0.3339 |
| gross_profit_factor | 0.7313 |
| gross_win_rate | 0.4128 |
| sharpe_ratio | -16.4007 |
| sortino_ratio | -8.5823 |
| max_drawdown | 1.0000 |
| cagr | -0.9916 |
| net_avg_win | 4.5975 |
| net_avg_loss | -14.1525 |
| avg_hold_time_bars | 1.9353 |
| exposure | 0.1110 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
