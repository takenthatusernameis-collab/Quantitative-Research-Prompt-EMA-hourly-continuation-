# EMA Hourly Continuation — DAG/USDT P12_100

**Symbol:** DAG/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 802 |
| net_profit_factor | 0.5363 |
| net_win_rate | 0.4414 |
| gross_profit_factor | 0.8045 |
| gross_win_rate | 0.4451 |
| sharpe_ratio | -5.5495 |
| sortino_ratio | -2.1805 |
| max_drawdown | 0.9371 |
| cagr | -0.6631 |
| net_avg_win | 30.5469 |
| net_avg_loss | -45.0069 |
| avg_hold_time_bars | 13.4352 |
| exposure | 0.4898 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
