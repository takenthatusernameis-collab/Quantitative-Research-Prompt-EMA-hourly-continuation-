# EMA Hourly Continuation — FLUX/USDT P34_100

**Symbol:** FLUX/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 687 |
| net_profit_factor | 0.5692 |
| net_win_rate | 0.4687 |
| gross_profit_factor | 0.8921 |
| gross_win_rate | 0.4731 |
| sharpe_ratio | -4.4901 |
| sortino_ratio | -1.6590 |
| max_drawdown | 0.8713 |
| cagr | -0.5472 |
| net_avg_win | 35.4290 |
| net_avg_loss | -54.9068 |
| avg_hold_time_bars | 7.8239 |
| exposure | 0.2443 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
