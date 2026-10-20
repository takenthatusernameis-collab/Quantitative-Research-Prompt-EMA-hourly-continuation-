# EMA Hourly Continuation — METIS/USDT P50_55

**Symbol:** METIS/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 802 |
| net_profit_factor | 0.1644 |
| net_win_rate | 0.3192 |
| gross_profit_factor | 0.5670 |
| gross_win_rate | 0.3878 |
| sharpe_ratio | -12.9239 |
| sortino_ratio | -5.4174 |
| max_drawdown | 0.9994 |
| cagr | -0.9465 |
| net_avg_win | 7.6782 |
| net_avg_loss | -21.9033 |
| avg_hold_time_bars | 1.9327 |
| exposure | 0.0705 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
