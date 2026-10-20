# EMA Hourly Continuation — GALA/USDT P34_55

**Symbol:** GALA/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 903 |
| net_profit_factor | 0.3940 |
| net_win_rate | 0.4075 |
| gross_profit_factor | 0.7406 |
| gross_win_rate | 0.4230 |
| sharpe_ratio | -8.8791 |
| sortino_ratio | -3.7921 |
| max_drawdown | 0.9912 |
| cagr | -0.8443 |
| net_avg_win | 17.4987 |
| net_avg_loss | -30.5531 |
| avg_hold_time_bars | 3.2226 |
| exposure | 0.1323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
