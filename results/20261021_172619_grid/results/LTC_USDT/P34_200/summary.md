# EMA Hourly Continuation — LTC/USDT P34_200

**Symbol:** LTC/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.6158 |
| net_win_rate | 0.4573 |
| gross_profit_factor | 0.8083 |
| gross_win_rate | 0.4573 |
| sharpe_ratio | -2.3481 |
| sortino_ratio | -0.5716 |
| max_drawdown | 0.5224 |
| cagr | -0.2310 |
| net_avg_win | 57.7806 |
| net_avg_loss | -79.0713 |
| avg_hold_time_bars | 36.7509 |
| exposure | 0.4895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
