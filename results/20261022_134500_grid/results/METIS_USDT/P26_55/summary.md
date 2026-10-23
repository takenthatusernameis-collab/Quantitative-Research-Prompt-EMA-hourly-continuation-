# EMA Hourly Continuation — METIS/USDT P26_55

**Symbol:** METIS/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 925 |
| net_profit_factor | 0.4764 |
| net_win_rate | 0.4443 |
| gross_profit_factor | 0.8670 |
| gross_win_rate | 0.4541 |
| sharpe_ratio | -7.3224 |
| sortino_ratio | -3.1261 |
| max_drawdown | 0.9811 |
| cagr | -0.7886 |
| net_avg_win | 21.6868 |
| net_avg_loss | -36.4035 |
| avg_hold_time_bars | 4.3600 |
| exposure | 0.1833 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
