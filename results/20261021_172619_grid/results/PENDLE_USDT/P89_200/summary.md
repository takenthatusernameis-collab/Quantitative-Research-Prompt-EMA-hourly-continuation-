# EMA Hourly Continuation — PENDLE/USDT P89_200

**Symbol:** PENDLE/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 282 |
| net_profit_factor | 0.6523 |
| net_win_rate | 0.4504 |
| gross_profit_factor | 0.7880 |
| gross_win_rate | 0.4504 |
| sharpe_ratio | -2.0292 |
| sortino_ratio | -0.4831 |
| max_drawdown | 0.4622 |
| cagr | -0.1992 |
| net_avg_win | 63.1632 |
| net_avg_loss | -79.3357 |
| avg_hold_time_bars | 14.8901 |
| exposure | 0.1909 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
