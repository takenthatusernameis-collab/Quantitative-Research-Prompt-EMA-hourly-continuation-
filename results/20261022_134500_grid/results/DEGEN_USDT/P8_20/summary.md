# EMA Hourly Continuation — DEGEN/USDT P8_20

**Symbol:** DEGEN/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1554 |
| net_profit_factor | 0.5473 |
| net_win_rate | 0.4228 |
| gross_profit_factor | 0.8652 |
| gross_win_rate | 0.4421 |
| sharpe_ratio | -10.0288 |
| sortino_ratio | -5.5514 |
| max_drawdown | 0.9990 |
| cagr | -0.9358 |
| net_avg_win | 18.3809 |
| net_avg_loss | -24.5998 |
| avg_hold_time_bars | 3.2864 |
| exposure | 0.2325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
